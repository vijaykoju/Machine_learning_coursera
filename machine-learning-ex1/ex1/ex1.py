import numpy as np
import matplotlib.pylab as plt

data = np.genfromtxt('ex1data1.txt', delimiter=',')
X = np.ones([len(data[:,0]),2])
X[:,1] = data[:,0]
y = data[:,1]

plt.plot(X[:,1],y,'rx')
plt.xlabel('Population of City in 10,000s')
plt.ylabel('Profit in $10,000s')
plt.xlim(4,24)
plt.show()
