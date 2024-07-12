import numpy as np
import math

# p1
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(f"p1 answer: {a+b} and {a-b}")

# p2
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(a)
print(f"p2 answer: {a+b} and {a-b}")

# p3
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(f"p3 answer: {np.dot(a,b)}")

# p4
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8, 9, 10], [11, 12, 13, 14], [15, 16, 17, 18]])
print(f"p4 answer: {np.dot(a, b)}")

# p5
a = np.array([1, 2, 3])
print(f"p5 answer: {np.linalg.norm(a)}")

# p6
a = np.array([[1, 2], [3, 4]])
print(f"p6 answer: {a.T}")
