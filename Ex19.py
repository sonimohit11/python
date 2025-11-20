# Implement this for the system H(z)=0.5(z-0.7)(z-0.9)/(z-0.6)(z-0.4)  and verify whether the system is stable or unstable.

import sympy as sp

def z_transform_unit_step():
    n, z = sp.symbols('n z')
    x = sp.Heaviside(n)  

    Xz = sp.summation(x * z**(-n), (n, 0, sp.oo))
    Xz_simplified = sp.simplify(Xz)
    
    print("Z-transform of unit step:")
    print("X(z) =", Xz_simplified)

    poles = sp.solve(sp.denom(Xz_simplified), z)
    print("\nPoles:", poles)

    stable = all(abs(p) < 1 for p in poles)
    print("\nSystem Stability:", "Stable" if stable else "Unstable")

z_transform_unit_step()

# Write a Python function to compute the Z-transform of an unit step function. verify whether the system is stable or unstable. 

import numpy as np
from scipy.signal import dlti

def analyze_system():
    num = [0.5, -0.8, 0.315]  
    
    den = [1, -1.0, 0.24]

    system = dlti(num, den)

    poles = system.poles
    zeros = system.zeros

    print("Zeros:", zeros)
    print("Poles:", poles)

    stable = all(abs(p) < 1 for p in poles)
    print("\nSystem Stability:", "Stable" if stable else "Unstable")

analyze_system()