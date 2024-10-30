import pandas as pd
from matplotlib import pyplot as plt

df=pd.DataFrame({'x':range(-5,10)})
df['y'] = 1*df['x']**2 +4 - 4*df['x']

plt.plot(df.x,df.y,color='grey')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.axhline()
plt.axvline()
plt.show()