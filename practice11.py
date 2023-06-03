import numpy as np

X = np.array([1.0, .5])
W1 = np.array([[.1, .3, .5], [.2, .4, .6]])
B1 = np.array([.1, .2, .3])

print(W1.shape)
print(X.shape)
print(B1.shape)

A1 = np.dot(X, W1)+B1
print(A1)
