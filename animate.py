import gizeh
import numpy as np
import moviepy.editor as mpy
import itertools, math

W,H = np.array([256,256])*2 # width, height, in pixels
#duration = 2 # duration of the clip, in seconds

### Load the data
import h5py
f_h5 = "points.h5"
h5 = h5py.File(f_h5,'r')
R = h5["points"][:]

R = R[:]

pt_N, root_N, _ = R.shape
#R = R.reshape((root_N,pt_N,2))

#fps = 40
fps = 80

duration = pt_N/fps - 1.0/fps
print "Duration:",duration

movie_i = itertools.count()
radius = 20

def make_frame(t):
    dx = np.array([W/2.,H/2.])

    i = movie_i.next()
    pts = R[i]
    surface = gizeh.Surface(W,H)
    #radius = W*(1+ (t*(duration-t))**2 )/6
    #print radius

    cx = np.sin(t/duration*(np.pi))
    c = (cx, 0.5, 0)

    
    for x,y in pts:
        xy = dx + [x,y]*dx/1.5
        circle = gizeh.circle(radius, xy = xy, fill=c)
        circle.draw(surface)
        
    return surface.get_npimage()

clip = mpy.VideoClip(make_frame, duration=duration)
clip.write_gif("circle.gif",fps=fps, opt="OptimizePlus", fuzz=10)


