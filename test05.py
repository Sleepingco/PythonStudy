# ar = [i for i in range(1, 100, 3)] # 파이썬에서만 존재하는 배열 만드는 방법
# ar2 = [i for i in range(0,1000,2)]
# print(ar)
# print(ar2)
#
# def prime():
#     primnum = []
#     for i in range(1000):
#         for j in range(2, i):
#             if i % j == 0: break
#         else:
#             primnum.append(i)
#     return primnum
#
#
# arList = prime()
# print(arList)
# print(len(arList))
#
# # 튜플 CRUD중 UD불가 속도가 빠름
# t1 = 1, 2, 3, 4, 5
# t2 = 'Hello', 3.14, -1, True
# for x in t2:
#     print(x)
# print(t1)
# print(len(t1))  # max(), min(), t.count(), t.index()
# print(t2)
# # t1[0] = -1 xxxxxxxxxxx
#
# # set (집합) 중복불가 중복된값을 지워주니 중간 필터로 많이씀 인덱스가 존재 안해서 리스트로 만들어서 출력해야함
# s1 = {1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1}
# for x in s1:
#     print(x)
# s2 = {5, 6, 7, 8, 9, 10}
# print(s1)
# print(s2)
# s3=s1.union(s2) # 합치기
# print(s3)
# s3=s1.intersection(s2) # 겹치는 값
# print(s3)
# s3=s1.difference(s2) # 다른값
# print(s3)
# # R
# li=list(s1) # len(),min(),max(),sum(), l1=s1.sorted()
# print(li[3])
# s1.add
# # U
# # s1.update(리스트)
# # D
# # s1.clear()
# # s1.discard(값)
#
# # dictionary
# d1 = {3.14: 'pi', 'e': 1.023}
# print(d1)
# print(d1[3.14])
# print(d1['e'])
# d2 = {'name': 'John', 'age': 23, 'city': 'Goyang', 'birthday': '20030617', 20: "20's"}
# for x in d2:
#     print(x, d2[x])  # 키값과 벨류를 따로 써야함
# for k, v in d2.items():
#     print(k, v)  # 이렇게 출력하면 튜플을 리턴함
# print(d2[20])
# d3 = {'list': [1, 2, 3, 4, 5],
#       'tuple': {1, 2, 3, 4, 5},
#       'set': {1, 2, 3, 4, 5},
#       'dict': {'name': 'ilsan', 'city': 'cheonan'}}
# print(d3['list'])
# print(d3['tuple'])
# print(d3['set'])
# print(d3['dict'])
# print(d3['dict']['name'])
# l4 = [{'name': 'John', 'age': 23}, {'name': 'Jane', 'age': 21}, {'name': 'Jason', 'age': 35}]
# for x in l4:
#     print(x['name'], x['age'])

