import math
# name  = input('이름을 입력하시오')
# print('이름',name)
# age=int(input('나이를입력하시오'))
# if age=='':
#     age=0
# # age = int(age)
# print(type(age))
# print('나이',age)
# print('^--^ '*100)

# # 1000이하의 소수(Prime Number)구하기
# for i in range(2, 1000, 1):
#     for j in range(2, i-1, 1):
#         if i % j == 0:
#             break
#     else:
#             print(i)

# for i in range(2, 1001, 1):
#     for j in range(2, i, 1):
#         if i % j == 0:
#             break
#         if j == i-1:
#             print(i)
#
# # -- 피라미드 출력
#
# for i in range(11):
#     print('*' * i)
# for j in range(11, 0, -1):
#     print('*' * j)

# # 최소공배수 최대공약수
# i = int(input('값1 입력'))
# j = int(input('값2 입력'))
# if i > j:
#     for k in range(1, j+1, 1):
#         if j % k == 0 and i % k == 0:
#             a = i / k
#             b = j / k
#             q = 1
#             q = q * k
#     else:
#         print(q,int(q*a*b))
# if i < j:
#     for k in range(1, i+1, 1):
#         if i % k == 0 and j % k == 0:
#             a = i / k
#             b = j / k
#             q = 1
#             q = q * k
#     else:
#         print(q,int(q*a*b))

# # 최소공배수 최대공약수
# a = int(input('값1 입력'))
# b = int(input('값2 입력'))
# x = 1
# while True:
#     if b<a:
#         a,b=b,a
#     for i in range(2,a+1):
#         if a%i==0 and b%i==0:
#             x*=i
#             a//=i
#             b//=i
#             break
#     else:
#         break
# print('최대공약수=',x)
# print('최소공배수',x*a*b)

# a,b,c,값을 읽어서 이차방정식의 근(해)를 구하기
# a = int(input('a: '))
# b = int(input('b: '))
# c = int(input('c: '))
# x1 = (-b+math.sqrt((b**2)-(4*a*c)))/(2*a)
# x2 = (-b-math.sqrt((b**2)-(4*a*c)))/(2*a)
# print(x1, '|', x2)

import math

a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

x1 = (-b + math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)
x2 = (-b - math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)

print(x1, '|', x2)
