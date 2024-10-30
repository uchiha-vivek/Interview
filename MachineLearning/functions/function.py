

import numpy as np
from matplotlib import pyplot as plt

def f(x):
    return x**2


x=np.array(range(-10,10))
print(x)


# setting up graph
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()

plt.plot(x,f(x),color='purple')
plt.show()