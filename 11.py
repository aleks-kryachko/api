# задание ЦФТ
import math

a = int(input())
b = int(input())
c = int(input())
m =max(a, b, c)
print(m)
if m == math.sqrt(a**2+b**2):

    print('прямоугольный')
else:
    print('не прямоугольный')

