import numpy as np 
import matplotlib.pyplot as plot

def shift(x,r):
    a_n=np.roll(x,r)
    if(r<0):
        for i in range(7+r,7,1):
            a_n[i]=0
    else:
        for i in range(0,r,1):
            a_n[i]=0
    return a_n
x=[2,4,-3,1,-5,4,7]  
n=np.arange(-3,4,1)
xby3=shift(x,3)  
xbym4=shift(x,-4)
x2=2*np.array(xby3)
x3=3*np.array(xbym4)
x1=np.add(x2,x3)
x1=np.subtract(x1,x)
plot.stem(n,x1)
plot.show() 

#part2
def reverse(a_n):
        for i in range(0,3,1):
            temp=a_n[i]
            a_n[i]=a_n[6-i]
            a_n[6-i]=temp
        return a_n
x=[2,4,-3,1,-5,4,7]      
xrev=reverse(x)    
xbym4=shift(xrev,-4)    
xby4=shift(xrev,4)
xf_n=np.add(xbym4,xby4)
plot.stem(n,xf_n)
plot.show()

#part3
n=np.arange(-3,4,1)
x_n=[2,4,-3,1,-5,4,7] 
u_n=np.zeros(7)
for i in range(0,7,1):
    if(i>=3):
        u_n[i]=1
x=reverse(u_n)
y=shift(x,-1)
x1=x_n*y
x2=2*np.array(x1)
plot.stem(n,x2)
plot.show()