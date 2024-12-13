import math
a = 2
b = 3
c = 4

s = (a + b + c) / 2  # 半周長
print(math.sqrt(s * (s - a) * (s - b) * (s - c)))