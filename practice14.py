import numpy as np

a = np.array([.3, 2.9, 4.0])

exp_a = np.exp(a)
print(exp_a)

sum_exp_a = np.sum(exp_a)
print(sum_exp_a)

y = exp_a / sum_exp_a
print(y)

# 위의 코드는 softmax 함수를 구현한 것 입니다.
