import matplotlib.pyplot as plt
import numpy as np
import random

xpoints = np.array([0, 80])
ypoints = np.array([0, 80])

xscatterpoints = [random.randrange(20, 60, 1) for i in range(15)]
yscatterpoints = [random.randrange(20, 60, 1) for i in range(15)]

plt.plot(xpoints, ypoints, 'b')
plt.plot(xscatterpoints, yscatterpoints, 'xg')

plt.show()

