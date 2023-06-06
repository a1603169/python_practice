import numpy as np


def identify_function(x):
    return x


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


X = np.array([1.0, .5])
W1 = np.array([[.1, .3, .5], [.2, .4, .6]])
B1 = np.array([.1, .2, .3])

A1 = np.dot(X, W1)+B1

Z1 = sigmoid(A1)

W2 = np.array([[.1, .4], [.2, .5], [.3, .6]])
B2 = np.array([.1, .2])


A2 = np.dot(Z1, W2) + B2
Z2 = sigmoid(A2)
print(Z2, Z2.shape)

W3 = np.array([[.1, .3], [.2, .4]])
B3 = np.array([.1, .2])

A3 = np.dot(W3, Z2) + B3
Y = identify_function(A3)

print(Y)

# The above is a 3-layer neural network. 이런식으로 하나하나씩 통과하여서 보여지는 것 입니다.
