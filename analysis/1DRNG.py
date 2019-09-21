# import sobol_seq
# from random import random
import matplotlib.pyplot as plt
from numpy import random
import chaospy as cp

plt.subplot(3, 5, 1)
a = random.uniform(-2, 2, 100)
plt.hist(a, density=True, bins=30)
plt.title("\n\nN=100")
plt.ylabel("Uniform")
plt.yticks([])
plt.xticks([])

plt.subplot(3, 5, 2)
a = random.uniform(-2, 2, 500)
plt.hist(a, density=True, bins=30)
plt.title("N=500")
plt.yticks([])
plt.xticks([])


plt.subplot(3, 5, 3)
a = random.uniform(-2, 2, 1000)
plt.hist(a, density=True, bins=30)
plt.title("N=1000")
plt.yticks([])
plt.xticks([])

plt.subplot(3, 5, 4)
a = random.uniform(-2, 2, 2000)
plt.hist(a, density=True, bins=30)
plt.title("N=2000")
plt.yticks([])
plt.xticks([])

plt.subplot(3, 5, 5)
a = random.uniform(-2, 2, 5000)
plt.hist(a, density=True, bins=30)
plt.title("N=5000")
plt.yticks([])
plt.xticks([])


plt.subplot(3, 5, 6)
b = random.normal(size =100)
plt.hist(b, density=True, bins=30)
plt.ylabel("Pseudorandom\nNumber Generation\n\n\nNormal")
plt.yticks([])
plt.xticks([])


plt.subplot(3, 5, 7)
b = random.normal(size=500)
plt.hist(b, density=True, bins=30)
plt.yticks([])
plt.xticks([])

plt.subplot(3, 5, 8)
b = random.normal(size=1000)
plt.hist(b, density=True, bins=30)
plt.yticks([])
plt.xticks([])

plt.subplot(3, 5, 9)
b = random.normal(size=2000)
plt.hist(b, density=True, bins=30)
plt.yticks([])
plt.xticks([])

plt.subplot(3, 5, 10)
b = random.normal(size= 5000)
plt.hist(b, density=True, bins=30)
plt.yticks([])
plt.xticks([])

plt.subplot(3, 5, 11)
c = random.exponential(size= 100)
plt.hist(c, density=True, bins=30)
plt.ylabel("Exponential")
plt.yticks([])
plt.xticks([])

plt.subplot(3, 5, 12)
c = random.exponential(size= 500)
plt.hist(c, density=True, bins=30)
plt.yticks([])
plt.xticks([])

plt.subplot(3, 5, 13)
c = random.exponential(size= 1000)
plt.hist(c, density=True, bins=30)
plt.yticks([])
plt.xticks([])

plt.subplot(3, 5, 14)
c = random.exponential(size= 2000)
plt.hist(c, density=True, bins=30)
plt.yticks([])
plt.xticks([])

plt.subplot(3, 5, 15)
c = random.exponential(size= 5000)
plt.hist(c, density=True, bins=30)
plt.yticks([])
plt.xticks([])

plt.show()
plt.savefig('1DRNG.png')

plt.subplot(3, 5, 1)
uni = cp.J(cp.Uniform(0,1))
p = uni.sample(100,rule="S")
plt.hist(p, density=True, bins=30)
plt.title("\n\nN=100")
plt.ylabel("Uniform")
plt.yticks([])
plt.xticks([])

plt.subplot(3, 5, 2)
uni = cp.J(cp.Uniform(0,1))
p = uni.sample(500,rule="S")
plt.hist(p, density=True, bins=30)
plt.title("\n\nN=500")
plt.yticks([])
plt.xticks([])

plt.subplot(3, 5, 3)
uni = cp.J(cp.Uniform(0,1))
p = uni.sample(1000,rule="S")
plt.hist(p, density=True, bins=30)
plt.title("\n\nN=1000")
plt.yticks([])
plt.xticks([])

plt.subplot(3, 5, 4)
uni = cp.J(cp.Uniform(0,1))
p = uni.sample(2000,rule="S")
plt.hist(p, density=True, bins=30)
plt.title("\n\nN=2000")
plt.yticks([])
plt.xticks([])

plt.subplot(3, 5, 5)
uni = cp.J(cp.Uniform(0,1))
p = uni.sample(5000,rule="S")
plt.hist(p, density=True, bins=30)
plt.title("\n\nN=5000")
plt.yticks([])
plt.xticks([])

plt.subplot(3, 5, 6)
uni = cp.J(cp.Normal(0,1))
p = uni.sample(100,rule="S")
plt.hist(p, density=True, bins=30)
plt.ylabel("Quasirandom\nNumber Generation\n\n\nNormal")
plt.yticks([])
plt.xticks([])

plt.subplot(3, 5, 7)
uni = cp.J(cp.Normal(0,1))
p = uni.sample(500,rule="S")
plt.hist(p, density=True, bins=30)
plt.yticks([])
plt.xticks([])

plt.subplot(3, 5, 8)
uni = cp.J(cp.Normal(0,1))
p = uni.sample(1000,rule="S")
plt.hist(p, density=True, bins=30)
plt.yticks([])
plt.xticks([])

plt.subplot(3, 5, 9)
uni = cp.J(cp.Normal(0,1))
p = uni.sample(2000,rule="S")
plt.hist(p, density=True, bins=30)
plt.yticks([])
plt.xticks([])

plt.subplot(3, 5, 10)
uni = cp.J(cp.Normal(0,1))
p = uni.sample(5000,rule="S")
plt.hist(p, density=True, bins=30)
plt.yticks([])
plt.xticks([])

plt.subplot(3, 5, 11)
uni = cp.J(cp.Exponential())
p = uni.sample(100,rule="S")
plt.hist(p, density=True, bins=30)
plt.ylabel("Exponential")
plt.yticks([])
plt.xticks([])

plt.subplot(3, 5, 12)
uni = cp.J(cp.Exponential())
p = uni.sample(500,rule="S")
plt.hist(p, density=True, bins=30)
plt.yticks([])
plt.xticks([])

plt.subplot(3, 5, 13)
uni = cp.J(cp.Exponential())
p = uni.sample(1000,rule="S")
plt.hist(p, density=True, bins=30)
plt.yticks([])
plt.xticks([])

plt.subplot(3, 5, 14)
uni = cp.J(cp.Exponential())
p = uni.sample(2000,rule="S")
plt.hist(p, density=True, bins=30)
plt.yticks([])
plt.xticks([])

plt.subplot(3, 5, 15)
uni = cp.J(cp.Exponential())
p = uni.sample(5000,rule="S")
plt.hist(p, density=True, bins=30)
plt.yticks([])
plt.xticks([])

plt.show()
plt.savefig('1DPD_RNG.png')