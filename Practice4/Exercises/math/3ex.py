import math
n = int(input())
base = int(input())
S = (n * base*base)/4*math.tan(math.pi/n)
print(round(S))