# 함수
import math


# def call(a,b,c):
#     return a+b+c
# x = call(3, 6, 8)
# print(x)
#
# def minus(a,b,c):
#     print(a-b-c)
# minus(10,7,5)

# 이차방정식의 근(해)을 구하는 함수 정의 & 호출
def solve(a, b, c):
    x = b ** 2 - 4 * a * c
    if x <= 0:
        return 0, 0
    x1 = (-b + math.sqrt(x)) / (2 * a)
    x2 = (-b - math.sqrt(x)) / (2 * a)
    return x1, x2


a, b = solve(1, -3, 2)
print('x1=', a, 'x2= ', b)

# 알고리즘이 안떠오르면 2시간이내 상사한테 꼭 물어보기
# 시킨일에대해 모르겠으면 30분안에 물어보기
