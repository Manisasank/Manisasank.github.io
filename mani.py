import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# -----------------------------
# Surface Plot Data
# -----------------------------
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

X, Y = np.meshgrid(x, y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

# -----------------------------
# 3D Scatter Data
# -----------------------------
np.random.seed(7)

cluster1 = np.random.randn(50,3) + np.array([2,2,2])
cluster2 = np.random.randn(50,3) + np.array([-2,-2,0])
cluster3 = np.random.randn(50,3) + np.array([2,-2,-2])

# -----------------------------
# Figure
# -----------------------------
fig = plt.figure(figsize=(14,6))

# Surface Plot
ax1 = fig.add_subplot(121, projection='3d')

surface = ax1.plot_surface(
    X, Y, Z,
    cmap='viridis',
    edgecolor='none'
)

ax1.set_title("3D Surface Plot")
ax1.set_xlabel("X")
ax1.set_ylabel("Y")
ax1.set_zlabel("Z")

ax1.view_init(elev=30, azim=45)

fig.colorbar(surface, ax=ax1, shrink=0.6)

# Scatter Plot
ax2 = fig.add_subplot(122, projection='3d')

ax2.scatter(cluster1[:,0], cluster1[:,1], cluster1[:,2],
            color='red', label='Cluster 1')

ax2.scatter(cluster2[:,0], cluster2[:,1], cluster2[:,2],
            color='blue', label='Cluster 2')

ax2.scatter(cluster3[:,0], cluster3[:,1], cluster3[:,2],
            color='green', label='Cluster 3')

ax2.set_title("3D Scatter Plot")
ax2.set_xlabel("X")
ax2.set_ylabel("Y")
ax2.set_zlabel("Z")

ax2.legend()

plt.tight_layout()
plt.show()