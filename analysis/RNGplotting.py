import sobol_seq
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
plt.xticks([])

plt.subplot(252)
prB = [(random(), random()) for _ in range(500)]
x_B = [x[0] for x in prB]
y_B = [x[1] for x in prB]
plt.scatter(x_B, y_B, s=1, marker=",")
plt.title("N=500")
plt.yticks([])
plt.xticks([])

plt.subplot(253)
prC = [(random(), random()) for _ in range(1000)]
x_C = [x[0] for x in prC]
y_C = [x[1] for x in prC]
plt.scatter(x_C, y_C, s=1, marker=",")
plt.title("N=1000")
plt.yticks([])
plt.xticks([])

plt.subplot(254)
prD = [(random(), random()) for _ in range(2000)]
x_D = [x[0] for x in prD]
y_D = [x[1] for x in prD]
plt.scatter(x_D, y_D, s=1, marker=",")
plt.title("N=2000")
plt.yticks([])
plt.xticks([])

plt.subplot(255)
prE = [(random(), random()) for _ in range(5000)]
x_E = [x[0] for x in prE]
y_E = [x[1] for x in prE]
plt.scatter(x_E, y_E, s=1, marker=",")
plt.title("N=5000")
plt.yticks([])
plt.xticks([])

plt.subplot(256)
qrA=sobol_seq.i4_sobol_generate(2,100)
x_F = [x[0] for x in qrA]
y_F = [x[1] for x in qrA]
plt.scatter(x_F, y_F, s=1, marker=",")
plt.ylabel("Quasirandom\nNumber Generation")

plt.subplot(257)
qrB=sobol_seq.i4_sobol_generate(2,500)
x_G = [x[0] for x in qrB]
y_G = [x[1] for x in qrB]
plt.scatter(x_G, y_G, s=1, marker=",")
plt.yticks([])

plt.subplot(258)
qrC=sobol_seq.i4_sobol_generate(2,1000)
x_H = [x[0] for x in qrC]
y_H = [x[1] for x in qrC]
plt.scatter(x_H, y_H, s=1, marker=",")
plt.yticks([])

plt.subplot(259)
qrD=sobol_seq.i4_sobol_generate(2,2000)
x_I = [x[0] for x in qrD]
y_I = [x[1] for x in qrD]
plt.scatter(x_I, y_I, s=1, marker=",")
plt.yticks([])

plt.subplot(2,5,10)
qrE=sobol_seq.i4_sobol_generate(2,5000)
x_J = [x[0] for x in qrE]
y_J = [x[1] for x in qrE]
plt.scatter(x_J, y_J, s=1, marker=",")
plt.yticks([])



plt.savefig('RNG.png')
plt.show()
