import itertools, multiprocessing
import numpy as np
import mpmath as mp
import h5py
import tqdm

f_h5 = "points.h5"

total_points = 10000
t0, t1 = 0, 10

periods = [0,2,3,5,7,11,13]
periods = np.array(periods,dtype=float)
use_sqrt = True
mp.dps = 15; mp.pretty = True

def coeffs(t):
    global periods

    if use_sqrt:
        periods = np.sqrt(periods)
    
    return np.array([np.cos(p*t) for p in periods]).T

def croots(co):
    return [mp.mpc(x) for x in mp.polyroots(co)]

T = np.linspace(t0,t1,total_points)
C = coeffs(T)

ITR = itertools.imap(croots, C)

MP = multiprocessing.Pool()
ITR = MP.imap(croots, C,chunksize=20)

R = []
for pts in tqdm.tqdm(ITR,total=total_points):
    pts = [map(float, (x.real, x.imag)) for x in pts]
    pts = np.array(pts)
    R.append(pts)

h5 = h5py.File(f_h5,'w')
h5["points"] = R
h5.close()
#R = list(ITR)
exit()

#import seaborn as sns
import pylab as plt


for Z in zip(*R):
    X = np.array([float(x.real) for x in Z])
    Y = np.array([float(x.imag) for x in Z])

    idx = np.abs(Y)>0.0001
    #X = X[idx]
    #Y = Y[idx]

    print X.shape

    n = len(Z)
    TC = (T-T.min())/T.max()
    TC = np.linspace(0,1,n)
    COLORS = np.array([TC,TC[::-1],np.ones(n)*0.5]).T
    

    plt.scatter(X,Y,c=COLORS,lw=0,alpha=0.75)

plt.show()


