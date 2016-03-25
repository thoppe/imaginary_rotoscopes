# Imaginary Rotoscopes

Rotoscoping the motion of roots across the complex plane.

## Moving image


<img src="https://raw.githubusercontent.com/thoppe/imaginary_rotoscopes/master/figures/alternate.gif" width=400"/>

    [ 0.  2.  3.  2.  4.  2.  5.  2.  6.]

## Static image
  
Work in progress example:

    n=6
    q=[0,2,3,5,7,11,13]
    f=cos(sqrt(q)*t)
    t=linspace(0,10, 10000)

![](figures/simple_6.png)
