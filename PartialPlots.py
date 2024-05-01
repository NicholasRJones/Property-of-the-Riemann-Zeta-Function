import numpy as np
import matplotlib.pyplot as plt
import mpmath as mp

"""""""""
This file shows what appears to be a peculiar property of the Riemann zeta function.
Namely, the distance from the nth partial sum of the p-series and the zeta function multiplied by the norm of the nth term 
of the partial sum appears to be monotonic when numerical noise does not interfere.
"""""""""


def partialsum(s, p, n):
    partial = np.zeros(n, dtype=complex)
    position = np.zeros(n + 1, dtype=complex)
    r = []
    i = []
    k = 0
    if p == 1:
        measure = mp.zeta(s)
    else:
        measure = 0
    while k < n:
        difference = (1 / (k + 1)) ** s
        position[k + 1] = position[k] + difference
        r.append(position[k + 1].real)
        i.append(position[k + 1].imag)
        if k > 0:
            partial[k] = abs(difference * (position[k + 1] - measure))
        k += 1
    plt.plot(r, i, color="maroon")
    plt.show()
    xinput = np.linspace(1, n + 1, n)
    plt.plot(xinput, partial, color="maroon")
    plt.show()


partialsum(1 / 2 + 14.134725j, 1, 10000)
