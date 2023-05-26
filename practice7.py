import numpy as np
import matplotlib.pylab as plt
# x = np.array([-1.0, 2.0, 3.0])
# print(x)
# y = x > 0
# print(y)
# y = y.astype(int)
# print(y)


def step_function(x):  # 계단 함수 입니당
    return np.array(x > 0, dtype=int)


x = np.arange(-5.0, 5.0, 0.1)
y = step_function(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()
