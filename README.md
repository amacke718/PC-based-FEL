# My PC based FELs
This process was used to visualize the FEL of local protein regions that were characterized with StELa (https://github.com/DimaUClab/StELa-Protein-Structure-Clustering-Algorithm)

**S**econdary S**t**ructure **E**nsembles with Machine **L**e**a**rning

Published by: Amanda C. Macke - Dima Group @ University of Cincinnati
email for questions (amacke718@gmail.com)

StELa's flagship publication was:

where we used StELa to identify a ligand dependent conformational transition in a local region of the severing enzymes Katanin and Spastin.

We then compared its capabilities with other clustering-based algorithms in the following article:
bioRxv - 

We wanted to know how well each discussed method characterized the conformational space observed during simulation. These FEL's were used to determine this. In a previous publication by Cheung et al (https://doi.org/10.1021/acs.jpcb.8b08852) they described the free energy landscapes with a polymer scientist's favorite reaction coordinates (Rg & Ree); however we found these to be insufficient CVs. That being said, the following procedure can also be adapted to visualized the FEL in Rg & Ree space as well.

###################################################################################### 
## A Letter from StELa 
######################################################################################

Dear User, 

If you want to visualize and understand the conformational landscape of your system, it is very important to consider the descriptors of said space. One way machine learning techniques have made our lives easier is by providing dimension reduction tools that can be used on huge data sets - such as those produced by molecular dynamics simulations. In GROMACS, an essential dynamics analysis can be carried out (https://manual.gromacs.org/documentation/current/reference-manual/analysis/covariance-analysis.html) to identify those regions found to cover the most variance in the trajecotry. This can provide insight into those dominant motions that we find the most interesting as follows:

> gmx covar -f $TRAJ -s $GRO -o eigenvalues.xvg -v eigenvectors.trr -xpma covapic.xpm

> gmx anaeig -f $TRAJ -s $GRO -v eigenvectors.trr -last 1 -proj pc1.xvg

> gmx anaeig -f $TRAJ -s $GRO -v eigenvectors.trr -first 2 -last 2 -proj pc2.xvg

We then can use some bash to combine these files:
> paste pc1.xvg pc2.xvg  | awk '{print $1,$2,$4}' > ${NAME}-PC1PC2.xvg

Use GROMACS to calculate the Free Energy:
> gmx sham -f ${NAME}-PC1PC2.xvg -ls FES.xpm

This creates an .xpm file that can be converted into a .dat file with code sourced from google!
python2.7 xpm2txt.py -f FES.xpm -o free-energy-landscape.dat

Then we use Python to Plot it!
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

