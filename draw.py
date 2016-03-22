#import seaborn as sns
import numpy as np
import pylab as plt
import h5py

f_h5 = "points.h5"
h5 = h5py.File(f_h5,'r')
R = h5["points"][:]

pt_N, root_N, _ = R.shape
R = R.reshape((root_N,pt_N,2))

for Z in R:
    X,Y = Z.T

    idx = np.abs(Y)>0.0001
    print X.shape

    n = len(Z)
    TC = np.linspace(0,1,n)
    COLORS = np.array([TC,TC[::-1],np.ones(n)*0.5]).T   

    plt.scatter(X,Y,c=COLORS,lw=0,alpha=0.75)

plt.show()


