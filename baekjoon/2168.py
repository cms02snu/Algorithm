# 2168

import math

x,y = map(int,input().split())
g = math.gcd(x,y)
print(x+y-g)