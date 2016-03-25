import itertools, multiprocessing
import numpy as np
import mpmath as mp
import h5py
import tqdm
import fractions

gcd = np.frompyfunc(fractions.gcd, 2, 1)
f_h5 = "points.h5"
twopi = 2*np.pi


t0, t1 = 0, twopi
total_points = 400

use_sqrt = False
repeats = True
phase = None

# Ordered 15
periods = np.arange(15)/2.0
periods[0] = 0

# Alternating
periods = np.array([0,2,3,2,4,2,5,2,6])

# Unity
periods = np.ones(10,dtype=float)
periods[0] = 0

# Signs
periods = [0,1,-1,2,-2,3,-3,4,-4,5,-5]
periods[0] = 0

# wigglewigglewiggle
periods = np.random.uniform(size=50)*(50/10.0) * 2 -1
periods[0] = 0

# Unity with 2phase
periods = np.ones(15,dtype=float)
periods[0] = 0
phase = np.linspace(0,twopi*2,periods.size)

# wigglewigglewiggle with 2phase
periods = np.random.uniform(size=50)*(50/10.0) * 2 -1
periods[0] = 0
phase = np.linspace(0,twopi*2,periods.size)

if phase is None:
    phase = np.zeros(periods.shape)

print "T0/T1/total points", t0,t1,total_points
print list(periods)

mp.dps = 12; mp.pretty = True

def coeffs(t):
    global periods, phase

    if use_sqrt:
        periods = np.sqrt(periods)
    
    return np.array([np.cos(p*t+a) for p,a in zip(periods,phase)]).T

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
ITR = MP.imap(croots, C,chunksize=1)

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
