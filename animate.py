import gizeh
import numpy as np
import moviepy.editor as mpy
import itertools, math

box = 128
fps = 40

### Load the data
import h5py
f_h5 = "points.h5"
h5 = h5py.File(f_h5,'r')
R = h5["points"][:]
pt_N, root_N, _ = R.shape
#duration = pt_N/float(fps)
duration = 10

print "Duration:",duration
print "pt_N", pt_N

def make_frame(t):
    
    W,H = np.array([box,box]) # width, height, in pixels
    radius = (box/256.0)*10
    surface = gizeh.Surface(W,H)

    i = int((t/duration)*pt_N)
    dx = np.array([W/2.,H/2.])
    pts = R[i]

    cx = np.sin(t/duration*(np.pi))
    c = (cx, 0.5, 0,0.75)
    
    for x,y in pts:
        xy = dx + [x,y]*dx/1.5

        scale = box/128.

        circle = gizeh.circle(radius+(2*scale), xy=xy, fill=[1,1,1,0.75])
        circle.draw(surface)

        circle = gizeh.circle(radius+(1*scale), xy=xy, fill=[0,0,0,1])
        circle.draw(surface)
        
        circle = gizeh.circle(radius, xy=xy, fill=c)
        circle.draw(surface)

    img = surface.get_npimage()
    return img 


clip = mpy.VideoClip(make_frame, duration=duration)
clip.write_gif("circle.gif",fps=fps, opt="OptimizePlus", fuzz=20)

box *= 4
clip = mpy.VideoClip(make_frame, duration=duration)

clip.write_videofile(
    "circle.mp4",
    fps=fps,
    threads=4,
    audio=False,
    preset='slow',
)



