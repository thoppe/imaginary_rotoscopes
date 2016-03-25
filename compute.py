import itertools, multiprocessing
import numpy as np
import mpmath as mp
import h5py
import tqdm
import fractions

gcd = np.frompyfunc(fractions.gcd, 2, 1)
f_h5 = "points.h5"

t0, t1 = 0, 6
periods = np.array([0,2,3,2,4,2,5,2,6])

#total_points = int(((t1-t0)/4)*slowdown)
total_points = 400
print "T0/T1/total points", t0,t1,total_points
print list(periods)

use_sqrt = False
repeats = True

#periods /= 5
periods = np.arange(15)/2.0
periods[0] = 0
#periods = np.ones(10)


#use_sqrt = False

#if repeats:
#    total_points *= 2

#periods = [0,2,3,5,7,11,13,17,19,23]
#use_sqrt = True

mp.dps = 12; mp.pretty = True

def coeffs(t):
    global periods

    if use_sqrt:
        periods = np.sqrt(periods)
    
    return np.array([np.cos(p*t) for p in periods]).T

def croots(co):
    return [mp.mpc(x) for x in mp.polyroots(co)]

periods = np.array(periods,dtype=float)
T = np.linspace(t0,t1,total_points)

#if repeats:
#    T = np.hstack([T,T[::-1]])


C = coeffs(T)

print periods

ITR = itertools.imap(croots, C)
MP = multiprocessing.Pool()
ITR = MP.imap(croots, C,chunksize=20)

R = []
for pts in tqdm.tqdm(ITR,total=total_points):
    pts = [map(float, (x.real, x.imag)) for x in pts]
    pts = np.array(pts)
    R.append(pts)

R = np.array(R)

if repeats:
    R = np.vstack([R,R[::-1]])

        

h5 = h5py.File(f_h5,'w')
h5["points"] = R
h5.close()
