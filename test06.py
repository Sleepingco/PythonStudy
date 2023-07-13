# 람다표현식(간단한 함수 만드는 방법)
# 함수명 = lambda 매개변수1,..,매개변수N: 반환값 계산코드
import math
#
# f = lambda x,y: x+y
# e = lambda x:x+10
# def x(x,y): # 함수 x 와 f는 같은 기능을 하는 함수이다
#     return x+y
# print(f(2,15))
# print(x(2,15))
#
around = lambda r: 2*math.pi*r # 둘레
square = lambda r: math.pi*r**2 # 넓이
volume = lambda r: 4/3*math.pi*r**3 # 체적,부피

radius = float(input('반지름[단위:m]'))
print('둘레 ',around(radius),'\n면적 ',square(radius), '\n체적', volume(radius))

quadratic_formula = lambda a,b,c:((-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a),(-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a))
a = float(input('a'))
b = float(input('b'))
c = float(input('c'))
print('X: ',quadratic_formula(a,b,c))