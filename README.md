# Imaginary Rotoscopes

Rotoscoping the motion of roots across the complex plane.

## Examples

   periods = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]

<img src="https://raw.githubusercontent.com/thoppe/imaginary_rotoscopes/master/figures/ordered_15.gif" width=256"/>

   periods = [0,1,1,1,1,1,1,1,1,1]

<img src="https://raw.githubusercontent.com/thoppe/imaginary_rotoscopes/master/figures/unity.gif" width=256"/>


    periods = [0,2,3,4,2,5,2,6]

<img src="https://raw.githubusercontent.com/thoppe/imaginary_rotoscopes/master/figures/alternate.gif" width=256"/>

## Static image
  
    n=6
    q=[0,2,3,5,7,11,13]
    f=cos(sqrt(q)*t)
    t=linspace(0,10, 10000)

![](figures/simple_6.png)
