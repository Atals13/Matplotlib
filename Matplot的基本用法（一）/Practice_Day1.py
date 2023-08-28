import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-1,2,5)
y=x-1
plt.figure(figsize=(8,8))
plt.plot(x,y,linestyle='--',linewidth='1.0')
plt.xlabel('THIS IS X')
plt.ylabel('THIS IS Y')
plt.xlim(-1,2)
plt.ylim(-2,2)
ax=plt.gca()#get the information of present axis
plt.xticks([-1,-0.5,1],['bad','normal','good'])
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))
#ax.xaxis.set_ticks_position('bottom')
#ax.yaxis.set_ticks_position('left')
plt.savefig('Practice_Day1.png',dpi=300,bbox_inches='tight')
plt.show()