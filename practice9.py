import numpy as np

A = np.array([[1, 2, 3, 4]])
B = np.array([[1], [2], [3], [4]])
C = np.array([[1, 2], [3, 4]])
D = np.array([[1, 2], [3, 4], [5, 6]])
E = np.array([[1, 2, 3], [4, 5, 6]])
F = np.array([[1, 2], [3, 4], [5, 6]])
G = np.array([7, 8])

print(A.shape)
print(B.shape)
print(C.shape)
print(D.shape)
print(E.shape)
print(F.shape)

print(np.ndim(A))
print(np.ndim(B))
print(np.ndim(C))
print(np.ndim(D))
print(np.ndim(E))
print(np.ndim(F))

print(np.dot(A, B))
# print(np.dot(C, D)) # Error
print(np.dot(E, F))
print(np.dot(D, G))
