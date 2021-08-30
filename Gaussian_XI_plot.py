import numpy as np
import matplotlib.pyplot as plt


sigma = 0.3
mu = 0



X = np.linspace(-3*sigma, 3*sigma, 500)

F_G = (1/(2*sigma*np.sqrt(2*3.14)))*np.exp(-np.power(X-mu, 2)/(2*sigma**2))
plt.plot(X, F_G, linewidth=3)
plt.grid()
plt.show()

