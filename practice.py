import numpy as np
a = np.zeros((1,4))
b = np.zeros((4,3))

c = a.dot(b)
print(c.shape)