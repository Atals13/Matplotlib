import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-3,3,50)
y=2*x+1
plt.plot(x,y,color='blue',linewidth='1.0')
ax=plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
x0=1
y0=2*x0+1
plt.plot([x0,x0],[0,y0],'k--',linewidth=2.5)
#normal:(x0,y0),(0,x0)----->[x0,x0],[0,y0]
plt.scatter([x0, ],[y0, ],s=50,color='b')
#scatter(**)**is the coordinate ,which use the same way as above
plt.annotate(r'2x+1=%s'%y0,xy=(x0,y0),xycoords='data',xytext=(+30,-30),
             textcoords='offset points',fontsize=16,
             arrowprops=dict(arrowstyle='->',connectionstyle="arc3,rad=.2"))
#too much too explain
plt.text(-3.7,3,r'this is some text. ',
         fontdict={'size':16,'color':'r'})
#text(coordinate,information)
plt.savefig('Annotation.png',dpi=300,bbox_inches='tight')
plt.show()