# - Menu명이 빈문자열이 입력될 때까지, MenuList를 작성 & 메뉴명/가격 목록 출력
# -- 모든 메뉴의 가격 합계 (리스트+딕셔너리)
# arMenu = [{},{},{}]
arMenu = []
sum1 = 0
# while True:
#     nName = str(input('메뉴명 입력'))
#     if nName == '':
#         for index, value in enumerate(arMenu):
#             print(index + 1, value)
#         print('합계', sum1)
#         break
#     nPrice = int(input('가격 입력'))
#     sum1 += nPrice
#     Menu = {'menu': nName}, {'price': nPrice}
#     arMenu.append(Menu)

# 강사님 코드
# while True:
#     nName = str(input('메뉴명 입력'))
#     if nName == '': break
#     d = {'menu': nName, 'price': int(input('가격입력'))}
#     arMenu.append(d)
# sum = 0
# for d in range(len(arMenu)):
#     print(f"{d['menu']} {d['price']}")
#     sum+=d['price']
# print(f'메뉴가격 합계 {sum}')
#
# arMenu = []

while True:
    nName = input('메뉴명 입력: ')
    if nName == '':
        break
    d = {'menu': nName, 'price': int(input('가격 입력: '))}
    arMenu.append(d)

sum = 0
for d in arMenu:
    print(f"{d['menu']} {d['price']}")
    sum += d['price']

print(f'메뉴 가격 합계: {sum}')