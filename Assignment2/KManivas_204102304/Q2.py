
import numpy as np
import matplotlib.pyplot as plt


start = -10
stop = 10
inc = 0.1
a =  np.arange(start,stop+inc,inc)
b =  np.arange(start,stop+inc,inc)
u = 0
sig = 1
E = np.zeros((len(b),len(a)))




# Varying a,b in the range [-10:0.1:10]

for i in range(len(b)):
    for j in range(len(a)):
    
        # Assigning 100 different points to x in the range [-10,10]
        x = np.linspace(-10,10,100)
        
        y = np.array([(2*k+3) for k in x])
        
        # Generate 100 points of Gaussian noise N(0,1)
        noise = np.random.normal(u,sig,100)
        
        # Add the noise to y to obtain actual values of y
        y_act = y + (sig*noise)
      
        
        # Calculate y for above values of x
        y_pred = np.array([(a[j]*k+b[i]) for k in x])
     
    
        e = y_act - y_pred
        
        # Calculate Mean Square Error for each value of a & b
        
        for m in range(len(e)):
            E[i][j] = E[i][j] + ((e[m])*(e[m]))
        E[i][j] = E[i][j]/len(e)


aa,bb = np.meshgrid(a,b)

print(aa.shape)
print(bb.shape)
print(E.shape)


fig = plt.figure()
ax1 = fig.add_subplot(111,projection='3d')
ax1.plot_surface(aa,bb,E)
ax1.set_xlabel('a values')
ax1.set_ylabel('b values')
ax1.set_zlabel('Error values(E)')
ax1.set_title('Surface Plot of Error function')
plt.grid()
plt.show()


    
    

