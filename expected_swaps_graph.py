from matplotlib import pyplot as plt
import numpy as np


# Estimated value E[S](n)
def e_s(n):
    return n - sum([1/i for i in range(1, n+1)])

# E[S](x) curve
x = list(range(1, 31))
y = [e_s(n) for n in x]
plt.plot(x, y, color='navy')
plt.text(x[-10], y[-12], 'E[S] for N=x', color='navy')

# y=x curve
# plt.plot(x, x, color='red')
# plt.text(x[-5], x[-1], 'y=x', color='red')

# Hand-calculated points
# plt.scatter(
#     [1, 2, 3, 4, 5], [0, 0.5, 7/6, 23/12, 163/60],
#     s=60,
#     color='white',
#     linewidths=2,
#     edgecolors='black'
# )

# Average distance between y=x and y=E[S](x)
# print(np.average(np.subtract(x, y)))

# Fit line
# m1, b1 = np.polyfit([1, 2, 3, 4, 5], [0, 0.5, 7/6, 23/12, 163/60], 1)
# plt.plot(x, np.add(np.multiply(x, m1), b1))
#
# m2, b2 = np.polyfit(x, y, 1)
# print(m2, b2)
# plt.plot(x, np.add(np.multiply(x, m2), b2))

# The y=x-3.128 line
# plt.plot(x, np.multiply(np.add(x, -3.128), 1), color='purple')
# print(np.average(np.square(np.subtract(y, np.add(x, -3.128)))))
# plt.text(x[-5], x[-10], 'y=x-3.128', color='purple')

# x-ln(x) curve
plt.plot(x, [x_ - np.log(x_) for x_ in x], color="red")
plt.text(x[-5], x[-10], 'y=x-ln(x)', color="red")

plt.show()
