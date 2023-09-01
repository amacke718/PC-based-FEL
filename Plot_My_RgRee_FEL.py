import matplotlib.pyplot as plt
import scipy.ndimage
import numpy as np
from scipy.ndimage import gaussian_filter
data = np.genfromtxt("free-energy-landscape.txt")

print(max(data[:,2]))
# Reshape for the contour plot
x_input = data[:,0]*10
x = x_input.reshape(32,-1)
x = gaussian_filter(x, sigma=.3)

y_input = data[:,1]*10
y = y_input.reshape(32,-1)
y = gaussian_filter(y, sigma=.3)

z = data[:,2].reshape(32,-1)
z = z * 0.239006
z = gaussian_filter(z, sigma=.3)
###################################################################################################
MY_FIG = plt.figure(figsize=(15,12))
# Will Normalize what you are plotting
m = plt.cm.ScalarMappable(cmap='jet')
plt.contour(x, y, z, 8, cmap='jet', linewidths=4) 
plt.grid(linestyle = '--', linewidth=1, color='k', alpha = 0.1)
plt.title('FEL of $R_{gyr}$ and $R_{ee}$\nWT', fontsize=30)
plt.xlabel(r'$R_{gyr}$ $\AA$', fontsize=36)
plt.xticks(fontsize=26)
plt.ylabel(r'$R_{ee}$ $\AA$', fontsize=36)
plt.yticks(fontsize=26)
cbar = plt.colorbar(m)   #boundaries=np.linspace(0, 1, 8)
for t in cbar.ax.get_yticklabels():
     t.set_fontsize(20)
     
plt.savefig('{0}_RGYR_REE_CONTOUR.png'.format(NAME), dpi=300)
