import numpy as np
import matplotlib.pyplot as plt

# parameters
a = 1.0
k = np.linspace(-6*np.pi/a, 6*np.pi/a, 1000)

# band indices (more bands due to folding)
m_values = range(-6, 7)
colors = plt.cm.rainbow(np.linspace(0, 1, len(m_values)))

plt.figure(figsize=(10, 6))

for i, m in enumerate(m_values):
    G = np.pi * m / a          # reciprocal lattice vector for 2a
    E = (k + G)**2
    plt.plot(k * a / np.pi, E,
             linewidth=2,
             color=colors[i],
             label=f"Band index m = {m}")

# Labels
plt.xlabel(r"$k$ (units of $\pi/a$)", fontsize=13)
plt.ylabel(r"$E_k$ (units of $\hbar^2/2ma^2$)", fontsize=13)

# Title
plt.title("Free-Electron Band Structure (Periodicity $2a$)",
          fontsize=14, fontweight="bold")

# Brillouin zone boundaries for 2a
for n in range(-12, 13):
    plt.axvline(n/2, color='gray', linestyle='--', alpha=0.4)

# Legend
plt.legend(title="Energy Bands",
           fontsize=9,
           title_fontsize=11,
           ncol=2)

# Grid and limits
plt.grid(True, alpha=0.3)
plt.xlim(-6, 6)
plt.ylim(0, 150)

plt.tight_layout()
plt.show()