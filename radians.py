import math

# градусы в радианы

x = 85  # x-в градусах
y = math.radians(x)

print(y)

print(round(y, 5))  # в радианах округлено до 5  символов после "."

# радианы в градусы

x = 85  # в радианах
y = math.degrees(x)
print(y)

print(round(y, 5))  #в градусах округлено до 5  символов после "."
