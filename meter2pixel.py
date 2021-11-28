from math import *

#number of pixels in a meter
alpha = radians(30)
d = 25
beta = radians(26.3)
h = 1080
l1 = 100
l2 = l1 + 1

x1 = h*(sin(0.5*alpha)+cos(0.5*alpha)*tan(atan(l1/d)+beta-radians(90)))/(sqrt(2*(1-cos(alpha))))
x2 = h*(sin(0.5*alpha)+cos(0.5*alpha)*tan(atan(l2/d)+beta-radians(90)))/(sqrt(2*(1-cos(alpha))))

print(x2-x1)