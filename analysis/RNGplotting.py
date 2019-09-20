# import sobol_seq
from random import random
import matplotlib.pyplot as plt
from matplotlib import gridspec

plt.subplot(251)
prA = [(random(), random()) for _ in range(100)]
x_A = [x[0] for x in prA]
y_A = [x[1] for x in prA]
plt.scatter(x_A, y_A, s=1, marker=",")
plt.ylabel("Pseudorandom\nNumber Generation")
plt.title("N=100")


plt.subplot(252)
prB = [(random(), random()) for _ in range(500)]
x_B = [x[0] for x in prB]
y_B = [x[1] for x in prB]
plt.scatter(x_B, y_B, s=1, marker=",")
plt.title("N=500")



plt.subplot(253)
prC = [(random(), random()) for _ in range(1000)]
x_C = [x[0] for x in prC]
y_C = [x[1] for x in prC]
plt.scatter(x_C, y_C, s=1, marker=",")
plt.title("N=1000")

plt.subplot(254)
prD = [(random(), random()) for _ in range(2000)]
x_D = [x[0] for x in prD]
y_D = [x[1] for x in prD]
plt.scatter(x_D, y_D, s=1, marker=",")
plt.title("N=2000")

plt.subplot(255)
prE = [(random(), random()) for _ in range(5000)]
x_E = [x[0] for x in prE]
y_E = [x[1] for x in prE]
plt.scatter(x_E, y_E, s=1, marker=",")
plt.title("N=5000")


plt.savefig('fig.png')
plt.show()
