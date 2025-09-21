import numpy as np
import pandas as pd

"""
TRANSFORM vs APPLY vs AGG in pandas (Deep Dive)
-----------------------------------------------

Mental model (shape-in / shape-out):
- groupby.agg  ➜  reduces each group to summary rows (fewer rows)
- groupby.transform  ➜  returns a result aligned to the original rows (same length)
- groupby.apply  ➜  do-anything hammer; you decide the return shape; usually slower

Quick when-to-use:
- Use .agg     → to summarize groups (mean, sum, min/max, multiple stats)
- Use .transform → to broadcast group stats back to each row (z-scores, fills, flags)
- Use .apply   → if you can't express it via agg/transform; last resort for complex logic

Core differences:
- Output shape:    agg: reduced; transform: unchanged; apply: flexible
- Speed:           agg/transform (vectorized) > apply (often Python-level)
- Stability:       agg/transform semantics are clearer and easier to optimize
- Function rules:  transform expects either a scalar per group or a same-length array
                   agg expects a scalar per group (or a small set via list/dict)
                   apply can return scalars, Series, or DataFrames

Common patterns:
- Within-group standardization (z-score):  (x - x.groupby(g).transform('mean')) / x.groupby(g).transform('std')
- Filling missing/invalid values with group stat:  x.fillna(x.groupby(g).transform('median'))
- Ranking inside groups:  df['rank_in_g'] = df.groupby(g)['val'].rank(method='dense')
"""

# ============================================================================
# Q31 — Patching negatives with a *group mean of positive values only*
# ============================================================================
# The expected output provided indicates the "group mean" excludes negatives:
#   Group A positives: 4, 8, 28, 12, 16  → mean = 13.6
#   Group B positives: 28                 → mean = 28.0
# So, for negatives we replace them with that positive-only group mean.

# Repro DataFrame
df = pd.DataFrame(
    {
        "vals": np.random.RandomState(31).randint(-30, 30, size=15),
        "grps": np.random.RandomState(31).choice(["A", "B"], 15),
    }
)

# ---------------------------
# Solution 1 (recommended): transform + mask (vectorized, readable)
# ---------------------------
pos_mean_by_group = df.groupby('grps')['vals'].transform(lambda s: s[s >= 0].mean())
df['patched_vals'] = np.where(df['vals'] < 0, pos_mean_by_group, df['vals'])
    
print("\nSolution 1 — transform + mask:")
print(df)

# ---------------------------
# Solution 2: agg/apply to compute mapping, then map + where
# (a) with .apply on the grouped Series to compute positive-only mean
# ---------------------------
pos_means_map_apply = df.groupby('grps')['vals'].apply(lambda s: s[s >= 0].mean())
df['patched_vals_via_applymap'] = df['vals'].where(df['vals'] >= 0, df['grps'].map(pos_means_map_apply))

# (b) with .agg via an auxiliary column (assign positives, then mean)
tmp = df.assign(pos=df['vals'].where(df['vals'] >= 0))
pos_means_map_agg = tmp.groupby('grps')['pos'].agg('mean')
df['patched_vals_via_aggmap'] = df['vals'].where(df['vals'] >= 0, df['grps'].map(pos_means_map_agg))

print("\nSolution 2 — via map from group stats (apply/agg paths):")
print(df[['vals','grps','patched_vals_via_applymap','patched_vals_via_aggmap']])

# ---------------------------
# Solution 3: groupby.apply returning a full DataFrame
# (more flexible but typically slower; good when you must reshape per group)
# ---------------------------
def patch_group(g: pd.DataFrame) -> pd.DataFrame:
    mean_pos = g.loc[g['vals'] >= 0, 'vals'].mean()
    g = g.copy()
    g['patched_vals_apply_df'] = np.where(g['vals'] < 0, mean_pos, g['vals'])
    return g

df_apply = df.groupby('grps', group_keys=False).apply(patch_group)

print("\nSolution 3 — groupby.apply returning a DataFrame:")
print(df_apply[['vals','grps','patched_vals_apply_df']])

# ============================================================================
# Edge cases & fallbacks
# - If a group has *no* positive values, the positive-only mean is NaN.
#   Decide your fallback: overall group mean? global mean? zero? leave as-is?
# Example fallback to the overall (all-values) group mean:
# ============================================================================
pos_mean = df.groupby('grps')['vals'].transform(lambda s: s[s >= 0].mean())
all_mean = df.groupby('grps')['vals'].transform('mean')
fallback = pos_mean.fillna(all_mean)  # use overall mean where pos-only mean is NaN
df['patched_vals_with_fallback'] = np.where(df['vals'] < 0, fallback, df['vals'])

# ============================================================================
# Cross-check against the target output
# ============================================================================
expected = pd.DataFrame(
    {
        "vals": [-12, -7, -14, 4, -7, 28, -2, -1, 8, -2, 28, 12, 16, -24, -12],
        "grps": list("ABAAA" "BAA" "BAAA" "AA"),  # "ABAAA" + "BAA" + "BAAA" + "AA" = 15 chars
        "patched_vals": [13.6, 28.0, 13.6, 4.0, 13.6, 28.0, 13.6, 13.6, 8.0,
                         28.0, 28.0, 12.0, 16.0, 13.6, 13.6],
    }
)
# Verify equality (values only; index may differ)
check = pd.concat(
    [
        df[['vals','grps','patched_vals']].reset_index(drop=True),
        expected[['vals','grps','patched_vals']]
    ],
    axis=1,
    keys=['got','exp']
)
print("\nSanity check (got vs exp):")
print(check)

# ============================================================================
# Bonus: If you actually wanted the mean of *all* values (including negatives)
# (this does NOT match the provided expected table; shown for clarity)
# ============================================================================
df['patched_allvals_mean'] = np.where(
    df['vals'] < 0,
    df.groupby('grps')['vals'].transform('mean'),  # includes negatives
    df['vals']
)

print("\nBonus — using mean of ALL values (different from expected):")
print(df[['vals','grps','patched_allvals_mean']])

# ============================================================================
# Reference cheatsheet
# ============================================================================
"""
Cheatsheet
----------
df.groupby(G)['x'].agg('mean')
    → One row per group; summarizes (reduce). Use named aggregation for multiple stats:
       df.groupby(G).agg(mean_x=('x','mean'), max_y=('y','max'))

df.groupby(G)['x'].transform('mean')
    → Same length as original; broadcasts per-group mean to each row (aligns by index).
      Great for fills, flags, and per-group normalization.

df.groupby(G).apply(func)
    → func receives each group (DataFrame or Series), returns anything (Series/DataFrame/scalar).
      Most flexible but often slower; prefer agg/transform if possible.

Pitfalls
--------
- transform must return either a scalar (broadcast) or a 1D array with the same length as the group.
- apply can unexpectedly change index order/levels; use group_keys=False when you want to avoid group labels in the index.
- Multi-agg with lists produces MultiIndex columns; prefer "named aggregation" for cleaner columns.
- Be explicit about edge cases (e.g., groups with no valid values for your stat).
"""
