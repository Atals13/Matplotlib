#Add legend: plt.legend()
#Scatter some points : plt.scatter()
#Add annotation: plt.annotate()
#Add some explanation:plt.text()
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-3,3,50)
y1=2*x+1
y2=x**2
l1,=plt.plot(x,y1,label='inner line')
l2,=plt.plot(x,y2,color='red',label='square line',linestyle='--')
#l1,l2 are lists
plt.xlim(-1,2)
plt.ylim(-2,3)
plt.yticks(np.linspace(-2,3,5),['really bad','bad','normal','good','really good'])
plt.xticks(np.linspace(-1,2,5))
plt.legend(handles=[l1,l2],loc=4)
#plt.legend() could modify the labels of  lines  using:labels=['eg1','eg2']
plt.savefig('legend.png',dpi=300,bbox_inches='tight')
plt.show()
