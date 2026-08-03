import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Enables 3D projection capabilities

# Set seed for reproducible cluster generation
np.random.seed(42)

# =========================================================
# 1. Data Preparation
# =========================================================
# Panel 1 Data: 2D Grid & Sinc Ripple Wave
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

# Radial distance function: Z = sin(R) / R
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R) / (R + 1e-5)  # 1e-5 prevents division by zero at the origin

# Panel 2 Data: 3 Distinct Clusters in 3D Space
cluster_1 = np.random.normal(loc=[-3, -3, -3], scale=0.8, size=(50, 3))
cluster_2 = np.random.normal(loc=[0, 3, 2], scale=0.8, size=(50, 3))
cluster_3 = np.random.normal(loc=[3, -2, 4], scale=0.8, size=(50, 3))

# =========================================================
# 2. Figure & Subplots Initialization
# =========================================================
fig, (ax1, ax2) = plt.subplots(
    1, 2, figsize=(15, 6), 
    subplot_kw={'projection': '3d'}
)

# ---------------------------------------------------------
# Panel 1: 3D Surface Plot
# ---------------------------------------------------------
surf = ax1.plot_surface(
    X, Y, Z, 
    cmap='viridis', 
    edgecolor='none', 
    antialiased=True
)

# Set required viewing angle: elevation=30°, azimuth=45°
ax1.view_init(elev=30, azim=45)

ax1.set_title('3D Ripple/Wave Surface Plot', fontsize=12, pad=12)
ax1.set_xlabel('X Axis')
ax1.set_ylabel('Y Axis')
ax1.set_zlabel('Z Axis')

# Add Colorbar mapped to Z-values
cbar = fig.colorbar(surf, ax=ax1, shrink=0.5, aspect=10, pad=0.1)
cbar.set_label('Z Value', rotation=270, labelpad=15)

# ---------------------------------------------------------
# Panel 2: 3D Scatter Plot
# ---------------------------------------------------------
ax2.scatter(
    cluster_1[:, 0], cluster_1[:, 1], cluster_1[:, 2], 
    color='crimson', label='Cluster 1', s=40, alpha=0.8
)
ax2.scatter(
    cluster_2[:, 0], cluster_2[:, 1], cluster_2[:, 2], 
    color='mediumseagreen', label='Cluster 2', s=40, alpha=0.8
)
ax2.scatter(
    cluster_3[:, 0], cluster_3[:, 1], cluster_3[:, 2], 
    color='royalblue', label='Cluster 3', s=40, alpha=0.8
)

# Match viewing angle for visual symmetry
ax2.view_init(elev=30, azim=45)

ax2.set_title('3D Scatter Plot (3 Clusters)', fontsize=12, pad=12)
ax2.set_xlabel('X Axis')
ax2.set_ylabel('Y Axis')
ax2.set_zlabel('Z Axis')
ax2.legend(loc='upper left')

# Render figure
plt.tight_layout()
plt.show()