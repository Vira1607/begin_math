import math

r = float(input())
m = float(input())

if 0.5 < abs(r) < abs(m) + 0.5:
  res = (4*r + 3*m)/(r**3 + m**2)*(math.sin(m**3)**2)
elif abs(r) > abs(m) + 0.5:
  res = (abs(r - m)**(0.5))*(math.cos(r**2)**3)
else:
  res = 'error'

print(res)

i = int(input())
a = 2.2
b = 0.3

if 7 <= i <= 12:
  if i < 10:
    y = a*(i**4) + b*i
  elif i == 10:
    y = math.tan(i + 0.5)
  else:
    y = math.exp(2*i) + ((a**2 + i**2)**(0.5))
  print(y)
else:
  print('значение i задано вне диапазона')
  if i < 7:
    print('число i меньше 7')
  else:
    print('число i больше 12')

