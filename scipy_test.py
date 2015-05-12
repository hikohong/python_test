#hiko test for science programming scipy

#%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return (x-3)*(x-5)*(x-7)+85

x = np.linspace(0, 10, 200)
y = f(x)

a, b = 1, 9
xint = x[np.logical_and(x>=a, x<=b)][::30]
yint = y[np.logical_and(x>=a, x<=b)][::30]


plt.plot(x, y, lw=2)
plt.axis([0, 10, 0, 140])
plt.fill_between(xint, 0, yint, facecolor='gray', alpha=0.4)
plt.text(0.5 * (a + b), 30,r"$\int_a^b f(x)dx$", horizontalalignment='center', fontsize=20);


#from __future__ import print_function
#from scipy.integrate import quad, trapz
#integral, error = quad(f, 1, 9)
#print("The integral is:", integral, "+/-", error)
#print("The trapezoid approximation with", len(xint), "points is:", trapz(yint, xint))


