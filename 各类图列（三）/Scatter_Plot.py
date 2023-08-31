import matplotlib.pyplot as plt
import numpy as np
n=1024
x=np.random.normal(0,1,n)
y=np.random.normal(0,1,n)
t=np.arctan2(x,y)
plt.scatter(x,y,s=75,c=t,alpha=.5)
plt.xlim(-1.5,1.5)
plt.ylim(-1.5,1.5)
plt.xticks(())
plt.yticks(())
plt.savefig('Scatter.png',dpi=300,bbox_inches='tight')
plt.show()