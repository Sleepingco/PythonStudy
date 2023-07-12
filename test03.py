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

#이차방정식의 근(해)을 구하는 함수 정의 & 호출
def solve1(a,b,c):
    x = b**2-4*a*c
    if x <= 0:
        return 0
    x1 = (-b + math.sqrt(x)) / (2 * a)
    return x1

def solve2(a,b,c):
    x = b ** 2 - 4 * a * c
    if x <= 0:
        return 0
    x2 = (-b - math.sqrt(x)) / (2 * a)
    return x2
x1 = solve1(1, -3, 2)
x2 = solve2(1, -3, 2)
print('x1=',x1,'\nx2=',x2)

# 알고리즘이 안떠오르면 2시간이내 상사한테 꼭 물어보기
#
# 시킨일에대해 모르겠으면 30분안에 물어보기
