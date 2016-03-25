import gizeh
import numpy as np
import moviepy.editor as mpy
import itertools, math

box = 128
W,H = np.array([box,]*2) # width, height, in pixels
#duration = 2 # duration of the clip, in seconds

### Load the data
import h5py
f_h5 = "points.h5"
h5 = h5py.File(f_h5,'r')
R = h5["points"][:]

pt_N, root_N, _ = R.shape
fps = 20
fps = 40

#duration = pt_N/fps - 1.0/fps

duration = pt_N/float(fps)
#duration = 10
print "Duration:",duration
print "pt_N", pt_N

duration = 10
radius = (box/256.0)*10


def make_frame(t):

    surface = gizeh.Surface(W,H)

    i = int((t/duration)*pt_N)
    #i = movie_i.next()
    
    dx = np.array([W/2.,H/2.])
    pts = R[i]


    cx = np.sin(t/duration*(np.pi))
    c = (cx, 0.5, 0,0.75)

    
    for x,y in pts:
        xy = dx + [x,y]*dx/1.5

        circle = gizeh.circle(radius+4, xy=xy, fill=[1,1,1])
        circle.draw(surface)

        circle = gizeh.circle(radius+2, xy=xy, fill=[0,0,0,1])
        circle.draw(surface)
        
        circle = gizeh.circle(radius, xy=xy, fill=c)
        circle.draw(surface)


        
        
    return surface.get_npimage()

clip = mpy.VideoClip(make_frame, duration=duration)

if pt_N<=500:
    clip.write_gif("circle.gif",fps=fps, opt="OptimizePlus", fuzz=20)

clip.write_videofile(
    "circle.mp4",
    fps=fps,
    threads=4,
    audio=False,
    preset='slow',
)



