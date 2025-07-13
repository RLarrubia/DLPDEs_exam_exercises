import numpy as np
import matplotlib.pyplot as plt


def solve_dpe(xs, E):
    f = 9.81  # cuerpo de fuerza por unidad de longitud

    # Cálculo de constantes de integración
    invE = 1.0 / E(xs)
    denom1 = np.trapz(invE, xs)          # ∫0^L 1/E(s) ds
    denom2 = np.trapz(xs * invE, xs)     # ∫0^L s/E(s) ds
    C1 = f * denom2 / denom1

    # Cálculo de u(x) mediante integración acumulativa
    ux = np.zeros_like(xs)
    for i, xi in enumerate(xs):
        si = xs[:i+1]
        integrand = (-f * si + C1) / E(si)
        ux[i] = np.trapz(integrand, si)

    return ux   
