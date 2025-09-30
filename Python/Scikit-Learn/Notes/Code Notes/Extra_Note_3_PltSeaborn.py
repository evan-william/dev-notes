"""
=================================================================
MATPLOTLIB & SEABORN - Data Visualization Guide
=================================================================

This file covers essential visualization techniques:
- Histograms with KDE
- Scatter plots with hue
- Bar charts (vertical and horizontal)
- Line plots
- Custom styling and color palettes
"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Set style for better-looking plots
sns.set_style("whitegrid")

# =================================================================
# 1. HISTOGRAMS WITH SEABORN
# =================================================================
print("=" * 60)
print("1. CREATING HISTOGRAMS")
print("=" * 60)

# Generate sample data
np.random.seed(42)
data = np.random.normal(100, 15, 1000)  # Mean=100, std=15, 1000 samples

# Create figure with subplots
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# Basic histogram
sns.histplot(data, bins=30, ax=axes[0])
axes[0].set_title('Basic Histogram')
axes[0].set_xlabel('Value')
axes[0].set_ylabel('Frequency')

# Histogram with KDE (Kernel Density Estimate)
sns.histplot(data, bins=30, kde=True, ax=axes[1])
axes[1].set_title('Histogram with KDE Overlay')
axes[1].set_xlabel('Value')
axes[1].set_ylabel('Frequency')

plt.tight_layout()
plt.savefig('histogram_example.png', dpi=100, bbox_inches='tight')
print("✓ Created histogram examples (saved as histogram_example.png)")
print("\nKDE (Kernel Density Estimate):")
print("- Smooth curve showing probability density")
print("- Helps visualize the distribution shape")
print("- Enable with kde=True parameter")
plt.close()


# =================================================================
# 2. CUSTOM TICK LABELS
# =================================================================
print("\n" + "=" * 60)
print("2. CUSTOM TICK LOCATIONS AND LABELS")
print("=" * 60)

# Create sample data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [150, 180, 220, 200, 250, 280]

plt.figure(figsize=(10, 5))
plt.plot(sales, marker='o', linewidth=2, markersize=8)

# Set custom x-axis ticks
tick_positions = [0, 1, 2, 3, 4, 5]
tick_labels = months
plt.xticks(tick_positions, tick_labels)

plt.title('Monthly Sales with Custom Labels')
plt.xlabel('Month')
plt.ylabel('Sales ($1000s)')
plt.grid(True, alpha=0.3)

plt.savefig('custom_ticks_example.png', dpi=100, bbox_inches='tight')
print("✓ Created custom tick labels example")
print("\nUsage: plt.xticks([positions], [labels])")
print("Example: plt.xticks([0, 1, 2], ['Jan', 'Feb', 'Mar'])")
plt.close()


# =================================================================
# 3. SCATTER PLOTS WITH HUE
# =================================================================
print("\n" + "=" * 60)
print("3. SCATTER PLOTS WITH COLOR BY CATEGORY (HUE)")
print("=" * 60)

# Create sample dataset
np.random.seed(42)
df = pd.DataFrame({
    'height': np.random.normal(170, 10, 150),
    'weight': np.random.normal(70, 15, 150),
    'gender': np.random.choice(['Male', 'Female'], 150)
})

# Add age category as third variable
df['age_group'] = np.random.choice(['Young', 'Middle', 'Senior'], 150)

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Scatter plot without hue
axes[0].scatter(df['height'], df['weight'], alpha=0.6)
axes[0].set_title('Basic Scatter Plot')
axes[0].set_xlabel('Height (cm)')
axes[0].set_ylabel('Weight (kg)')

# Scatter plot with hue (color by category)
sns.scatterplot(data=df, x='height', y='weight', hue='gender', 
                style='age_group', s=100, alpha=0.7, ax=axes[1])
axes[1].set_title('Scatter Plot with Hue (Gender) and Style (Age)')
axes[1].set_xlabel('Height (cm)')
axes[1].set_ylabel('Weight (kg)')

plt.tight_layout()
plt.savefig('scatter_hue_example.png', dpi=100, bbox_inches='tight')
print("✓ Created scatter plot with hue example")
print("\nThe 'hue' parameter:")
print("- Colors points based on a categorical variable")
print("- Automatically creates a legend")
print("- Syntax: sns.scatterplot(x='col1', y='col2', hue='category')")
plt.close()


# =================================================================
# 4. HORIZONTAL BAR CHARTS
# =================================================================
print("\n" + "=" * 60)
print("4. HORIZONTAL BAR CHARTS")
print("=" * 60)

# Sample data: Top programming languages
languages = ['Python', 'JavaScript', 'Java', 'C++', 'Go']
popularity = [85, 78, 72, 65, 60]

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Vertical bar chart
axes[0].bar(languages, popularity, color='skyblue', edgecolor='navy')
axes[0].set_title('Vertical Bar Chart')
axes[0].set_ylabel('Popularity Score')
axes[0].set_xlabel('Language')

# Horizontal bar chart
axes[1].barh(languages, popularity, color='lightcoral', edgecolor='darkred')
axes[1].set_title('Horizontal Bar Chart')
axes[1].set_xlabel('Popularity Score')
axes[1].set_ylabel('Language')

plt.tight_layout()
plt.savefig('bar_charts_example.png', dpi=100, bbox_inches='tight')
print("✓ Created bar chart examples")
print("\nUsage:")
print("- Vertical bars: plt.bar(x, height)")
print("- Horizontal bars: plt.barh(y, width)")
print("\nHorizontal bars are better when:")
print("- Category names are long")
print("- Comparing many categories")
plt.close()


# =================================================================
# 5. LINE PLOTS (MULTIPLE LINES)
# =================================================================
print("\n" + "=" * 60)
print("5. LINE PLOTS - OVERLAYING MULTIPLE LINES")
print("=" * 60)

# Sample data: Product sales over time
months = np.arange(1, 13)
product_a = [100, 120, 140, 130, 150, 170, 160, 180, 200, 190, 210, 230]
product_b = [80, 90, 95, 100, 110, 115, 120, 130, 140, 145, 150, 160]
product_c = [60, 70, 80, 85, 90, 100, 110, 120, 130, 140, 150, 165]

plt.figure(figsize=(12, 6))

# Plot multiple lines
plt.plot(months, product_a, marker='o', linewidth=2, label='Product A')
plt.plot(months, product_b, marker='s', linewidth=2, label='Product B')
plt.plot(months, product_c, marker='^', linewidth=2, label='Product C')

plt.title('Monthly Sales Comparison', fontsize=14, fontweight='bold')
plt.xlabel('Month', fontsize=12)
plt.ylabel('Sales (units)', fontsize=12)
plt.legend(loc='upper left', fontsize=10)
plt.grid(True, alpha=0.3)
plt.xticks(months)

plt.savefig('line_plots_example.png', dpi=100, bbox_inches='tight')
print("✓ Created multiple line plots example")
print("\nKey points:")
print("- Call plt.plot() multiple times to overlay lines")
print("- Use 'label' parameter for legend entries")
print("- Different markers: 'o' (circle), 's' (square), '^' (triangle)")
print("- plt.legend() displays the legend")
plt.close()


# =================================================================
# 6. COLOR PALETTES IN SEABORN
# =================================================================
print("\n" + "=" * 60)
print("6. APPLYING COLOR PALETTES")
print("=" * 60)

# Create sample categorical data
df = pd.DataFrame({
    'category': ['A', 'B', 'C', 'D', 'E'] * 20,
    'value': np.random.randint(10, 100, 100)
})

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Different palette examples
sns.boxplot(data=df, x='category', y='value', palette='Blues', ax=axes[0, 0])
axes[0, 0].set_title('Blues Palette')

sns.boxplot(data=df, x='category', y='value', palette='Reds', ax=axes[0, 1])
axes[0, 1].set_title('Reds Palette')

sns.boxplot(data=df, x='category', y='value', palette='viridis', ax=axes[1, 0])
axes[1, 0].set_title('Viridis Palette')

sns.boxplot(data=df, x='category', y='value', palette='Set2', ax=axes[1, 1])
axes[1, 1].set_title('Set2 Palette')

plt.tight_layout()
plt.savefig('color_palettes_example.png', dpi=100, bbox_inches='tight')
print("✓ Created color palette examples")
print("\nPopular Seaborn palettes:")
print("- Sequential: 'Blues', 'Greens', 'Reds', 'Purples'")
print("- Diverging: 'RdBu', 'coolwarm', 'Spectral'")
print("- Qualitative: 'Set1', 'Set2', 'Set3', 'Pastel1'")
print("- Perceptual: 'viridis', 'plasma', 'inferno', 'magma'")
print("\nUsage: palette='Blues' in any Seaborn plot function")
plt.close()


# =================================================================
# 7. COMPREHENSIVE EXAMPLE: SALES DASHBOARD
# =================================================================
print("\n" + "=" * 60)
print("7. COMPREHENSIVE VISUALIZATION DASHBOARD")
print("=" * 60)

# Generate realistic sales data
np.random.seed(42)
dates = pd.date_range('2024-01-01', '2024-12-31', freq='D')
sales_data = pd.DataFrame({
    'date': dates,
    'revenue': np.random.normal(10000, 2000, len(dates)) + 
               np.linspace(0, 5000, len(dates)),  # Upward trend
    'region': np.random.choice(['North', 'South', 'East', 'West'], len(dates)),
    'product': np.random.choice(['Widget', 'Gadget', 'Doohickey'], len(dates))
})

# Create dashboard
fig = plt.figure(figsize=(16, 10))
gs = fig.add_gridspec(3, 2, hspace=0.3, wspace=0.3)

# 1. Revenue over time (line plot)
ax1 = fig.add_subplot(gs[0, :])
monthly_revenue = sales_data.groupby(sales_data['date'].dt.to_period('M'))['revenue'].sum()
ax1.plot(range(len(monthly_revenue)), monthly_revenue.values, 
         marker='o', linewidth=2, color='darkblue')
ax1.set_title('Monthly Revenue Trend', fontsize=14, fontweight='bold')
ax1.set_xlabel('Month')
ax1.set_ylabel('Revenue ($)')
ax1.grid(True, alpha=0.3)
ax1.set_xticks(range(len(monthly_revenue)))
ax1.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                      'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# 2. Revenue distribution (histogram with KDE)
ax2 = fig.add_subplot(gs[1, 0])
sns.histplot(sales_data['revenue'], bins=50, kde=True, color='skyblue', ax=ax2)
ax2.set_title('Revenue Distribution', fontsize=12, fontweight='bold')
ax2.set_xlabel('Daily Revenue ($)')
ax2.set_ylabel('Frequency')

# 3. Revenue by region (horizontal bar)
ax3 = fig.add_subplot(gs[1, 1])
region_revenue = sales_data.groupby('region')['revenue'].sum().sort_values()
ax3.barh(region_revenue.index, region_revenue.values, color='lightcoral')
ax3.set_title('Total Revenue by Region', fontsize=12, fontweight='bold')
ax3.set_xlabel('Revenue ($)')

# 4. Product performance (scatter with hue)
ax4 = fig.add_subplot(gs[2, 0])
product_summary = sales_data.groupby(['product', 'region'])['revenue'].mean().reset_index()
sns.scatterplot(data=product_summary, x='product', y='revenue', 
                hue='region', s=200, alpha=0.7, ax=ax4)
ax4.set_title('Average Revenue: Product by Region', fontsize=12, fontweight='bold')
ax4.set_ylabel('Average Revenue ($)')

# 5. Regional comparison (box plot)
ax5 = fig.add_subplot(gs[2, 1])
sns.boxplot(data=sales_data, x='region', y='revenue', palette='Set2', ax=ax5)
ax5.set_title('Revenue Distribution by Region', fontsize=12, fontweight='bold')
ax5.set_ylabel('Revenue ($)')

plt.savefig('sales_dashboard.png', dpi=100, bbox_inches='tight')
print("✓ Created comprehensive sales dashboard")
print("\nThis dashboard demonstrates:")
print("- Line plot for trends")
print("- Histogram with KDE for distributions")
print("- Horizontal bar chart for comparisons")
print("- Scatter plot with hue for relationships")
print("- Box plot for statistical summaries")
plt.close()


# =================================================================
# SUMMARY AND BEST PRACTICES
# =================================================================
print("\n" + "=" * 60)
print("SUMMARY - MATPLOTLIB & SEABORN")
print("=" * 60)
print("""
Key Visualization Techniques:

1. Histograms:
   sns.histplot(data, bins=30, kde=True)
   - Show distribution of single variable
   - KDE adds smooth density curve

2. Scatter Plots:
   sns.scatterplot(x='col1', y='col2', hue='category')
   - Show relationship between variables
   - Hue adds color by category

3. Bar Charts:
   plt.bar(x, height)      # Vertical
   plt.barh(y, width)      # Horizontal
   - Compare categories

4. Line Plots:
   plt.plot(x, y, label='Series 1')
   - Show trends over time
   - Overlay multiple lines

5. Customization:
   - plt.xticks([positions], [labels])
   - palette='Blues' for color schemes
   - marker='o', linewidth=2 for styling

Best Practices:
- Always label axes and add titles
- Use legends for multiple series
- Choose appropriate chart types
- Apply consistent color schemes
- Consider colorblind-friendly palettes
- Save with dpi=100 or higher for quality

Common Plot Types by Use Case:
- Distribution: histogram, box plot, violin plot
- Comparison: bar chart, box plot
- Relationship: scatter plot, line plot
- Composition: pie chart, stacked bar
- Trend: line plot, area chart
""")