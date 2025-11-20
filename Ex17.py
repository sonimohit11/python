# Using Python, compute the Z-transform of the sequence x[n]=3^n u[n].
import sympy as sp

def z_transform_3n_unitstep():
    n, z = sp.symbols('n z')
    
    x = 3**n * sp.Heaviside(n)

    Xz = sp.summation(x * z**(-n), (n, 0, sp.oo))
    Xz_simplified = sp.simplify(Xz)

    print("Z-Transform of x[n] = 3^n u[n]:")
    print("X(z) =", Xz_simplified)
    poles = sp.solve(sp.denom(Xz_simplified), z)
    print("\nPoles:", poles)

    stable = all(abs(p) < 1 for p in poles)
    print("\nSystem Stability:", "Stable" if stable else "Unstable")
z_transform_3n_unitstep()

# Using Python, compute the Z-transform of the sequence x[n]=cos⁡(wn)u[n]. 

import sympy as sp

def ztransform_cos():
    n, z, w = sp.symbols('n z w', real=True)
    
    x = sp.cos(w*n) * sp.Heaviside(n)
    
    Xz = sp.summation(x * z**(-n), (n, 0, sp.oo))
    Xz_simplified = sp.simplify(Xz)
    
    print("Z-transform of x[n] = cos(w*n)u[n]:")
    print("X(z) =", Xz_simplified)
ztransform_cos()