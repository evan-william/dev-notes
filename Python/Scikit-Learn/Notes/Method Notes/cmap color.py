# 🔹 Matplotlib Colormap Categories & Names
# -----------------------------------------

# 1. Perceptually Uniform Sequential
#   - 'viridis', 'plasma', 'inferno', 'magma', 'cividis'

# 2. Sequential
#   - 'Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds'
#   - 'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu'
#   - 'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn'

# 3. Sequential (2) (often lighter versions)
#   - 'binary', 'gist_yarg', 'gist_gray', 'gray', 'bone'
#   - 'pink', 'spring', 'summer', 'autumn', 'winter', 'cool'
#   - 'Wistia', 'hot', 'afmhot', 'gist_heat', 'copper'

# 4. Diverging
#   - 'PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy'
#   - 'RdBu', 'RdYlBu', 'RdYlGn', 'Spectral', 'coolwarm', 'bwr', 'seismic'

# 5. Cyclic
#   - 'twilight', 'twilight_shifted', 'hsv'

# 6. Qualitative
#   - 'Pastel1', 'Pastel2', 'Paired', 'Accent'
#   - 'Dark2', 'Set1', 'Set2', 'Set3'
#   - 'tab10', 'tab20', 'tab20b', 'tab20c'

# 7. Miscellaneous
#   - 'flag', 'prism', 'ocean', 'gist_earth', 'terrain'
#   - 'gist_stern', 'gnuplot', 'gnuplot2', 'CMRmap'
#   - 'cubehelix', 'brg', 'gist_rainbow', 'rainbow', 'jet'
#   - 'nipy_spectral', 'gist_ncar'

# Example Usage:
plt.scatter(X_scaled[:,0], X_scaled[:,1], c=dbscan.labels_, cmap="Spectral")
