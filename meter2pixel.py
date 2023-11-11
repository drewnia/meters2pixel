from math import *

# number of pixels in a meter

RIGEL = False
h = 416  # FRAME height 4mp 1440, 2mp 1080, YOLO frame 416
w = 416  # FRAME width
dist = 1 # distance in meters, for which we would like to find pixels

alpha = radians(50)  # lens angle
d = 25  # height of a tower
beta = radians(26)  # angle of position

l2 = 110 # maximal distance

if RIGEL:
    alpha = radians(120)
    d = 10 # height of a rigel
    beta = radians(45)
    l2 = 70
l1 = l2 - dist
x1 = h * (sin(0.5 * alpha) + cos(0.5 * alpha) * tan(atan(l1 / d) + beta - radians(90))) / (sqrt(2 * (1 - cos(alpha))))
x2 = h * (sin(0.5 * alpha) + cos(0.5 * alpha) * tan(atan(l2 / d) + beta - radians(90))) / (sqrt(2 * (1 - cos(alpha))))

print(x1)
print(x2)
print("{} pt in {} meters".format(x2 - x1,dist))
