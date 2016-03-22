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
