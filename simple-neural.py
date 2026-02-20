import numpy as np

x = np.array([0.8, 0.5])
w = np.array([0.7, -0.6])
b = 0.1


z = np.dot(x, w) +  b

def step(z):
    return 1 if z > 0 else 0


y = step(z)

print("z", z)
print("y", y)


#z1: 0.36
#s1:  1


#z2: -1.4000000000000001
#s2:  0
