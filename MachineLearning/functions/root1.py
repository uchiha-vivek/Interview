# find sqrt/solution of y=3x**2-12
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import math

y=0
x1 = int(-math.sqrt(y+12/3))
x2 = int(math.sqrt(y+12/3))

# creating a dataframe
df=pd.DataFrame({'x':range(x1-10,x2+11)})
df['y'] = 3*df['x']**2-12

# get x at the line of symmetry
vx = (x1+x2)/2
vy = 3*vx**2 -12

# get min and max values 

miny = df.y.min()
maxy = df.y.max()

plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.axhline()
plt.axvline()
plt.plot(df.x,df.y,color='purple')
#plot line of symmetery
sx = [vx,vy]
sy = [miny,maxy]
plt.plot(sx,sy,color='magenta')
plt.show()
