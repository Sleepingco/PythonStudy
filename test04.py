# create
arName = [1, 'hello', 3.14, True, None, 'world']

arName.append(25)
arName.insert(3, '박성호')
# arName.extend(리스트) # 리스트와 리스트를 병합
# # read
# print('0', arName[0])
# print('1', arName[1])
# print('2', arName[2])
# print('3', arName[3])
# print('4', arName[4])
# print('5', arName[5])
# print('6', arName[6])
# print('7', arName[7])
# x = arName[3]
# print(type(x))

# update
# arName[3] = '하이미디어'

# delete
# arName.remove(3.14)  # 값으로 지우기
# arName.remove('하이미디어')
# del arName[3]  # 인덱스로 지우기
# x = arName.pop(3)  # 인덱스 위치의 값을 반환하고 삭제


# arName.clear()  # 리스트 전체를 비우기
#
# # 기타등등
# arName.sort()
# arName.reverse()

# for i in arName:
#   print(i)
# print('-' * 30)
# arName.reverse()
# for i in range(len(arName)):
#   print(i, '=', arName[i])

# arList를 reverse하는 코드 작성

# arList = [1, 3, 5, 7, 9, 11, 13, 15, 17]
# i = 0
# j = len(arList)-1
#
# while i < j:
#     arList[i], arList[j] = arList[j], arList[i]
#     i += 1
#     j -= 1
#
# print(arList)
# print('-'*30)
#
# for i in range(len(arList) - 1, -1, -1):
#     arStart = arList[i]
#     del arList[i]
#     arList.append(arStart)
#
# print(arList)

# 메뉴가격 빈문자열입력될때까지 입력 출력

arMenu = []
arPrice = []
while True:
    Menu = input('메뉴명 입력')
    arMenu.append(Menu)
    if Menu == '':
        for i in range(len(arMenu) - 1, len(arMenu) - 2, -1):
            del arMenu[i]
        print('메뉴',arMenu)
        sum1 = 0
        for i in range(-1, len(arMenu) - 1, 1):
            temp = arPrice[i]
            sum1 += temp
        print('가격',arPrice)
        print('합계', sum1)
        break
    Price = int(input('가격 입력'))
    arPrice.append(Price)
