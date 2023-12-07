
import math
theta = math.pi/4
theta = -1* math.pi/4
v = [1,1]

v = [math.cos(theta)*v[0]-math.sin(theta)*v[1],
                             math.sin(theta)*v[0]+math.cos(theta)*v[1]]

v[0] = -v[0]

v = [math.cos(-theta)*v[0]-math.sin(-theta)*v[1],
            math.cos(-theta)*v[1]+math.sin(-theta)*v[0]]

print(v)

#Inverse
