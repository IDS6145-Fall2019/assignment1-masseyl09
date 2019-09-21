# import sobol_seq
# from random import random
import matplotlib.pyplot as plt
from numpy import random

plt.subplot(6, 5, 1)
a = random.uniform(-2, 2, 100)
plt.hist(a, density=True, bins=30)


plt.subplot(6, 5, 2)
b = random.uniform(-2, 2, 500)
plt.hist(b, density=True, bins=30)
plt.yticks([])


plt.subplot(6, 5, 3)
c = random.uniform(-2, 2, 1000)
plt.hist(c, density=True, bins=30)
plt.yticks([])

plt.subplot(6, 5, 4)
d = random.uniform(-2, 2, 2000)
plt.hist(d, density=True, bins=30)
plt.yticks([])

plt.subplot(6, 5, 5)
e = random.uniform(-2, 2, 5000)
plt.hist(e, density=True, bins=30)
plt.yticks([])


plt.subplot(6, 5, 6)
f = random.normal(size =100)
plt.hist(f, density=True, bins=30)


plt.subplot(6, 5, 7)
g = random.normal(size=500)
plt.hist(g, density=True, bins=30)
plt.yticks([])


plt.subplot(6, 5, 8)
h = random.normal(size=1000)
plt.hist(h, density=True, bins=30)
plt.yticks([])

plt.subplot(6, 5, 9)
i = random.normal(size=2000)
plt.hist(i, density=True, bins=30)
plt.yticks([])

plt.subplot(6, 5, 10)
j = random.normal(size= 5000)
plt.hist(j, density=True, bins=30)
plt.yticks([])



plt.show()
