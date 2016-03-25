# Imaginary Rotoscopes

Rotoscoping the motion of roots across the complex plane.

## Examples

#### Ordered set
 
    periods = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]

<img src="https://raw.githubusercontent.com/thoppe/imaginary_rotoscopes/master/figures/ordered_15.gif" width=256"/>

#### Unity (boring)

    periods = [0,1,1,1,1,1,1,1,1,1]

<img src="https://raw.githubusercontent.com/thoppe/imaginary_rotoscopes/master/figures/unity.gif" width=256"/>


#### Unity (with phase shifts)

    periods = [0,1,1,1,1,1,1,1,1,1]
    phase = np.linspace(0,twopi*2,periods.size)

<img src="https://raw.githubusercontent.com/thoppe/imaginary_rotoscopes/master/figures/unity_phase.gif" width=256"/>
 

#### Alternating twos

    periods = [0,2,3,4,2,5,2,6]

<img src="https://raw.githubusercontent.com/thoppe/imaginary_rotoscopes/master/figures/alternate.gif" width=256"/>
 
#### Signs

    periods = [0,1,-1,2,-2,3,-3,4,-4,5,-5]

<img src="https://raw.githubusercontent.com/thoppe/imaginary_rotoscopes/master/figures/signs.gif" width=256"/>

#### wigglewigglewiggle

    periods = np.random.uniform(size=50)*(50/10.0) * 2 -1
    phase = np.linspace(0,twopi*2,periods.size)

<img src="https://raw.githubusercontent.com/thoppe/imaginary_rotoscopes/master/figures/wigglewigglewiggle.gif" width=256"/>

#### static trace over sqrt(primes)
  
    n=6
    q=[0,2,3,5,7,11,13]
    f=cos(sqrt(q)*t)
    t=linspace(0,10, 10000)

![](figures/simple_6.png)
