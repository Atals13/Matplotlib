#Define the frame: plt.figure()
#Draw: plt.plot(x,y)
#Define the range of the axis: plt.xlim()/plt.ylim()
#Define the name of two axis: plt.xlabel()/plt.ylabel()
#Define axis scales and names:plt.xticks()/plt.yticks()
#Define the boundary's color of figure: ax=plt.gca()//get the information of present axis
                                        #ax.spines['right or something else'].set_corlor('none’)
#Adjust the scale's position: ax.xaxis.set_ticks_position()
#Adjust the axis's position: ax.spines['right or something else'].set_position()
import matplotlib.pyplot as plt 
import numpy as np
x=np.linspace(-3,3,50)
y1=x*2+1
y2=x**2
#-----------------------------------
plt.figure(num=3,figsize=(9,5))
plt.plot(x,y1)
plt.plot(x,y2,color='red',linewidth=1.0,linestyle='--')
#-----------------Create the frame and draw
plt.xlim((-1,1))
plt.ylim((-2,3))
plt.xlabel('I am X')
plt.ylabel('I am Y')
#---------------Define the axis range and name
new_ticks=np.linspace(-1,1,5)
y_numbers=np.linspace(-2,3,5)
plt.xticks(new_ticks)
plt.yticks(y_numbers,['really bad','bad','normal','good','really good'])
#-------------Define the axis scale and name
ax=plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
#-----------Adjust color of the frame's border
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
#------------Adjust the position both the scale and spines
plt.savefig('Basic konwledge.png',dpi=300,bbox_inches='tight')
#-------------Save the figure and set dpi(分辨率) and position('tight'自适应)
plt.show()
