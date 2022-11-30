import math

r = float(input())
h = float(input())
v = float(input())
m = float(input())

V = r**2*math.pi*h
v = v*m

print(round(V-v,3) if V>=v else 0)