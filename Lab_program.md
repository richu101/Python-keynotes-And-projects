# Plot the graph of sin and cos
------------
import numpy as np
import matplotlib.pyplot as plt
x= np.arange(0,10,0.01)
y= np.sin(x)
z= np.cos(x)
plt.plot(y,label = "sin")
plt.plot(z,label = "cos")
plt.grid()
plt.title('sin and cos wave')
plt.legend()
plt.show()
