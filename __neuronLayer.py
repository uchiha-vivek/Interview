import numpy as np

inputs = np.random.randint(0,10,3)

weights = np.random.randint((4,3))

bias = np.random.randint(0,5,4)

output = np.dot(inputs,weights.T) + bias

print(output)



