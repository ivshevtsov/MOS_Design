import matplotlib.pyplot as plt
import math
plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"
plt.rcParams["figure.figsize"]=[4,8]


pi=3.1415
Q=[0.5,  0.707, 1, 10]

for i in Q:
    angle = math.acos(1/(2*i))*180/pi
    alpha = 1/(2*i)
    betta = 1*math.sqrt(1-1/(4*i**2))
    X = [0, -alpha]
    Y1 = [0,  betta]
    X_full = [-alpha, 0, -alpha]
    Y_full = [betta, 0,  -betta]
    plt.plot(X_full, Y_full, label=f'Q={i} $\Phi$={round(angle,1)}', linewidth=3)

plt.xlabel('Re')
plt.ylabel('Im')
plt.legend(loc=3)
plt.grid()
plt.show()
