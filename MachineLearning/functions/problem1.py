import numpy as np
from matplotlib import pyplot as plt

def g(x):
    if x is not 0:
        return (6/x)**2
    if x is None:
        return 1

x=np.array(range(-5,5))
print(x)
y=[ g(a) for a in x ]
print(y)
plt.xlabel(x)
plt.ylabel('g(x)')
plt.grid()

plt.plot(x,g(x),color='purple')