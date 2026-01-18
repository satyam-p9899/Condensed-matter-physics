import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eigh_tridiagonal

E0 = -5.0   #On site energy(eV)
b  = -1.0   # Hopping parameter beta(eV)

bins_w = [0.2, 0.1, 0.05]
N0 = [10,20, 50, 100,500]

for N in N0:

    #diagonal of hamiltonian
    diag = E0 * np.ones(N)
    offdiag = b * np.ones(N - 1)

    #Diagonalize
    eigvals, eigvecs = eigh_tridiagonal(diag, offdiag)

    #Fermi level (spin-degenerate, half-filled)
    E_F = 0.5 * (eigvals[N//2 - 1] + eigvals[N//2])

    #DOS
    bin_width = bins_w[0]
    Emin, Emax = eigvals.min(), eigvals.max()
    bins = np.arange(Emin, Emax + bin_width, bin_width)

    dos, edges = np.histogram(eigvals, bins=bins, density=True)
    energy_mid = 0.5 * (edges[:-1] + edges[1:])

    #Plot DOS
    plt.figure()
    plt.plot(energy_mid, dos, label=f"DOS (N={N})")
    plt.axvline(E_F, color='r', linestyle='--', label="Fermi level")
    plt.xlabel("Energy (eV)")
    plt.ylabel("Density of States")
    plt.legend()
    plt.title(f"DOS for 1D chain (N ={N} and bin width={bin_width} eV)")
    plt.savefig(f"DOS_N{N}_bin{bin_width}.png", dpi=300, bbox_inches="tight")
    plt.show()
    plt.close()

    # Eigenstates
    idx_min = 0
    idx_max = N - 1
    idx_homo= N//2 - 1
    idx_lumo= N//2

    sites = np.arange(1, N + 1)

    plt.figure()
    plt.plot(sites, eigvecs[:, idx_min], label="Minimum energy")
    plt.plot(sites, eigvecs[:, idx_homo],label="HOMO")
    plt.plot(sites, eigvecs[:, idx_lumo],label="LUMO")
    plt.plot(sites, eigvecs[:, idx_max], label="Maximum energy")

    plt.xlabel("Site index")
    plt.ylabel("Eigenstate amplitude")
    plt.legend()
    plt.title(f"Eigenstates of 1D chain (N = {N} and bin width={bin_width} eV)")
    plt.savefig(f"Eigenstates_N{N}.png", dpi=300, bbox_inches="tight")
    plt.show()
    plt.close()