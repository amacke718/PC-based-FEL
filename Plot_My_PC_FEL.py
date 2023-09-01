> ###################################################################################################

> import os

> import numpy as np

> import matplotlib.pyplot as plt

> import scipy.ndimage

> from scipy.ndimage.filters import gaussian_filter

> data = np.genfromtxt("free-energy-landscape.dat")

> x = data[:,0].reshape(32,-1)

> x = gaussian_filter(x, sigma=.7)

> y = data[:,1].reshape(32,-1)

> y = gaussian_filter(y, sigma=.7)

> z = data[:,2].reshape(32,-1)

> z = gaussian_filter(z, sigma=.7)

> ###################################################################################################

> MY_FIG = plt.figure(figsize=(15,12))

> m = plt.cm.ScalarMappable(cmap='CMRmap')

> plt.contour(x,y,z, 10, colors='k')

> plt.contourf(x,y,z, 10, cmap='CMRmap')

> #For Contour plot

> cbar = plt.colorbar(m, boundaries=np.linspace(0, 1, 11))

> for t in cbar.ax.get_yticklabels():

>    t.set_fontsize(20)

> plt.grid(linestyle = '--', linewidth=1, color='k', alpha = 0.2)

> plt.title('FEL of PC1 and PC2\nWater', fontsize=30)

> plt.xlabel('PC1', fontsize=36)

> plt.xticks(fontsize=26)

> plt.ylabel('PC2', fontsize=36)

> plt.yticks(fontsize=26)

> plt.xlim(np.min(x), np.max(x))

> plt.ylim(np.min(y), np.max(y))

> plt.savefig('{0}_PC1_PC2_CONTOUR.png'.format(NAME), dpi=300)
