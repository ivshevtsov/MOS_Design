import random
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"
plt.rcParams['lines.linewidth'] = 3


x_Circle = np.linspace(0, 1, 100)
y_Circle = (1-x_Circle**2)**0.5


N = 100000
x_Rand = []
y_Rand = []
x_Rand_Circle = []
y_Rand_Circle = []
sum=0
for i in range(N):
    x = random.random()
    y = random.random()
    x_Rand.append(x)
    y_Rand.append(y)
    if (x**2+y**2)**0.5<=1:
        x_Rand_Circle.append(x)
        y_Rand_Circle.append(y)
        sum = sum+1
pi = 4*sum/N
print(f'PI={pi}')
print(f'pi={np.pi}')
print(f'Error={100*(np.pi-pi)/np.pi}')

plt.figure(figsize=(6, 6), dpi=80)
plt.title(rf'$\pi$={round(pi, 5)}')
plt.plot(x_Rand, y_Rand, '.')
plt.plot(x_Rand_Circle, y_Rand_Circle, '.')
plt.plot(x_Circle, y_Circle, linewidth=5)
plt.xlabel('x')
plt.ylabel('y')
plt.show()