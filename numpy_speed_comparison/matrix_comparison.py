from datetime import datetime
import numpy as np

n = 20
a = np.random.randn(n, n)
b = np.random.randn(n, n)

times = 10000


def manual_multiplication(a, b):
    mul = np.zeros((n, n))
    for i in range(len(a)):
        for j in range(len(a)):
            for k in range(len(a)):
                mul[i][j] = mul[i][j] + a[i][k] * b[k][j]


def numpy_multiplication(a, b):
    mul = a.dot(b)


t0 = datetime.now()
for t in range(times):
    manual_multiplication(a, b)
dt1 = datetime.now() - t0

t0 = datetime.now()
for t in range(times):
    numpy_multiplication(a, b)
dt2 = datetime.now() - t0

print("dt1 / dt2", dt1.total_seconds() / dt2.total_seconds())
