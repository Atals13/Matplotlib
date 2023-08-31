import matplotlib.pyplot as plt
import numpy as np
a=np.linspace(0,1,9).reshape(3,3)
plt.imshow(a,interpolation='nearest',cmap='RdBu',origin='lower')
plt.colorbar(shrink=.92)
plt.xticks(())
plt.yticks(())
plt.savefig('matrix.png',dpi=400,bbox_inches='tight')
plt.show()