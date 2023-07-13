# - Menu명이 빈문자열이 입력될 때까지, MenuList를 작성 & 메뉴명/가격 목록 출력
# -- 모든 메뉴의 가격 합계 (리스트+딕셔너리)
# arMenu = [{},{},{}]
arMenu = []
sum1 = 0
while True:
    nName = str(input('메뉴명 입력'))
    if nName == '':
        for index, value in enumerate(arMenu):
            print(index + 1, value)
        print('합계', sum1)
        break
    nPrice = int(input('가격 입력'))
    sum1 += nPrice
    Menu = {'menu': nName}, {'price': nPrice}
    arMenu.append(Menu)
