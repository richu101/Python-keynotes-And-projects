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
# Richu 
