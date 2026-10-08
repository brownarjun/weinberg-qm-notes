"""Constants in cgs, matching Weinberg's conventions (Notation, pp. xxi-xxii).

Un-rationalized electrostatic units: Coulomb potential of charges e1, e2 is e1*e2/r.
Fine structure constant alpha = e^2 / (hbar*c) ~ 1/137.
"""

import numpy as np

# Fundamental
c      = 2.99792458e10          # speed of light, cm/s (exact)
kB     = 1.380649e-16           # Boltzmann constant, erg/K (exact)
h      = 6.62607015e-27         # Planck constant, erg s (exact)
hbar   = h / (2.0*np.pi)        # reduced Planck constant
e      = 4.80320427e-10         # electron charge (statC), |e|
me     = 9.1093837015e-28       # electron mass, g

# Derived (Weinberg Eq. 1.1.6 and p. 4)
alpha      = e**2 / (hbar * c)                    # ~ 1/137.036
a_B        = 8.0*np.pi**5 * kB**4 / (15.0 * h**3 * c**3)   # radiation density const
sigma      = c * a_B / 4.0                                 # Stefan-Boltzmann
a0         = hbar**2 / (me * e**2)                # Bohr radius, cm
Ryd        = me * e**4 / (2.0 * hbar**2)          # Rydberg energy, erg

if __name__ == "__main__":
    print(f"alpha      = {alpha:.6f}  (1/alpha = {1/alpha:.3f})")
    print(f"a_B        = {a_B:.5e} erg cm^-3 K^-4  [Weinberg: 7.56577e-15]")
    print(f"sigma      = {sigma:.5e} erg cm^-2 s^-1 K^-4  [Weinberg: 5.670373e-5]")
    print(f"a0         = {a0:.4e} cm")
    print(f"Ryd        = {Ryd:.4e} erg = {Ryd/1.602e-12:.4f} eV  [Weinberg: 13.6 eV]")
