# Python lab projects :boom:
 
# Q1
------------
 Plot the graph of sin and cos
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
# Q2

Factorial of a num
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

# Q3
-------
Write a python program to perform basic arithmetic functions such as 
abs, sine, real, imag, complex and using built in modules.

-------
```
import math
a=int(input("number"))
print(abs(a))
print(math.sin(math.radians (a)))
b=int(input("num2"))
c=complex(a,b)
print(c)
print(c.real)
print(c.imag)
```
# Q4
---------
Realize the functions sin t, and cos t for the vector t =[0; 10] with increment 
0:01.
---------
```
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0,10,0.01)
y = np.sin(x)
z=np.cos(x)
plt.plot(y,label='sin')
plt.plot(z,label='cos')
plt.legend()
plt.grid()
plt.title('cos and sin')
plt.show()
```

# Q5
-------
Write a python program to compute the first N Fibonacci numbers using 
function. 
--------
```
num=int(input("enter a number"))
first=0
sec=1
for i in range(num):
 c=first+sec
 t=first
 first=sec
 sec=c
print(t)
```

# Q6
-----------
Write a python program to plot the histogram of an image.
-----------
```
  from google.colab import files
  uploaded=files. upload()
```
```
import cv2
from matplotlib import pyplot as plt
png=cv2.imread('/content/Sc fibo.png')
plt.imshow(png)
plt.show()
color=cv2.cvtColor(png,cv2.COLOR_BGR2RGB)
plt.imshow(color)
plt.title('richu')
plt.show()  
```

# Q7 

Write a python program to Compute the rank and Eigen values of a 2x2 matrix

----------
```
import numpy as np

n=np.matrix([[5,-3],[-6,2]])
print(n)
print("\n")
ev=np.linalg.eig(n)
print(ev)
r=np.linalg.matrix_rank(n)
print(r)
```

# Q8
 
-----------
Plot histogram from an xlxs file
----------
```
from google.colab import files
uploaded=files.upload()
```

```
import matplotlib.pyplot as plt
import pandas as pd
files = pd.read_excel('/copypath.xlxs')
value = files['data']
plt.hist(files['data'])
plot.show()
```

# Q8

-------
Sum of n complex numbers
-------
```
def a(x):
 sum=0
 l=[] 
 for i in range(x):
   y=complex(input("num "))
   l.append(y)
 for i in range(x):
   sum=sum+l[i]

print("sum=",sum)
b= int(input("number"))
a(b)
```

# Q9
---------
Scatter ,hist,plot,bar of random data
---------
```
from matplotlib import pyplot as plt
import numpy as np
x=np.random.randn(10)
print(x)
plt.scatter(x,x)
```

# Tech.Rick 
