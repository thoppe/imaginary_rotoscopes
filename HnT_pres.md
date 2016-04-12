# <span style="text-transform: lowercase;">`imaginary rotoscopes`</span>
_or how I turned 200 years of complex analysis into a loading animation_
----------
### [Travis Hoppe](http://thoppe.github.io/)
[https://github.com/thoppe/imaginary_rotoscopes](https://github.com/thoppe/imaginary_rotoscopes)

====

let's break this down

## Imaginary
## Numbers

Squares root of minus one. $\sqrt{(-1)} = i$.

Often found when the quadratic equation goes boom!

# $\frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$

Any polynomials have complex roots equal to their degree.

# $ x^3 -x^2 -10 -8 =  (x+1)*(x-4)*(x+2)$
  
====*

let's break this down

## Rotoscopes
trace over footage, frame by frame

!(animations/aha.mp4)  <<height:410px;transparent>>
!(animations/face.gif) <<height:400px;transparent>>

====*

## Imaginary Rotoscopes
Draw over the roots of a polynomial as they
move through the complex plane!
### $ x^6 + \sin(\sqrt{2}t)x^5 + \sin(\sqrt{3}t)x^4 + \ldots ... $ 
!(figures/simple_6.png) <<height:420px>>

Animations? Use `gizeh` and `moviepy` to make animated gifs and mp4s.
  
====
  
## Unity (boring)
    periods = [0,1,1,1,1,1,1,1,1,1]
!(figures/unity.mp4) <<height:750px>>

====*

#### Unity (with phase shifts)

    periods = [0,1,1,1,1,1,1,1,1,1]
    phase = np.linspace(0,twopi*2,periods.size)
!(figures/unity_phase.mp4) <<height:750px>>

====

## Alternating twos
    periods = [0,2,3,4,2,5,2,6]
!(figures/alternate.mp4) <<height:750px>>

====*
  
## wigglewigglewiggle
    periods = np.random.uniform(size=50)*(50/10.0) * 2 -1
    phase = np.linspace(0,twopi*2,periods.size)
!(figures/wigglewigglewiggle.mp4) <<height:750px>>

====

#  Thanks, you!
Say hello: [@metasemantic](https://twitter.com/metasemantic)