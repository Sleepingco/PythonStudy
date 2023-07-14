# 재귀함수 recursivefunction 트리구조에서는 재귀함수를 쓸수있다

import sys

sys.setrecursionlimit(10 ** 8)


# def hundred(x):
#   sum = 0
#   for i in range(x, 0, -1):
#     sum += i
#   return sum
# print(hundred(100))
# def recur(x):  # 재귀함수는 반복문이 없다
#     if x == 1:
#         return 1
#     return x + recur(x - 1)
#
#
# print(recur(1000000))

def deffactor(x):  # 재귀함수는 반복문이 없다
    if x == 1:
        return 1
    return x * deffactor(x - 1)

print(deffactor(4))