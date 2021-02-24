# Plot the graph of sin and cos
------------
```
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
```

Fibanocii series
-----------
```
num=int(input("enter a number"))
f=1
if num <0:
  print('cant')
elif num==0:
  print('1')

else:

for i in range(1,num+1):
   f=f*i
print(f)
```
