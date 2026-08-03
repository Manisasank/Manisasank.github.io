#importing libraries which is required for sine and cosine plots
import numpy as np
import matplotlib.pyplot as plt

#here numpy used to work on numeric data(x values,sin,cos)
#matplotlib.pyplot is the plotting library-pyplot is its scripting interface
x=np.linspace(0, 2*np.pi, 100)
y_sin=np.sin(x)
y_cos=np.cos(x)

fig, ax=plt.subplots(figsize=(8, 5))
ax.plot(x, y_sin, color="blue", linewidth=2, linestyle="-",label="sin(x)")
ax.plot(x, y_cos, color="red", linewidth=2, linestyle="--", label="cos(x)")


ax.set_title("Sine,Cosine and Tangent Waves",fontsize=14, fontweight="bold")
ax.set_xlabel("x(radians)")
ax.set_ylabel("Amplitude")
ax.axhline(0, color="gray", linewidth=0.8)
ax.legend(loc="upper right")
ax.grid(True, linestyle="-",alpha=0.5)
plt.tight_layout()
plt.savefig("program1_sine_cosine_tangent_waves.png",dpi=150)
plt.show()