f = open('c:/temp/menu1.txt', 'r')
menulist = []
# armenu = f.readlines()
# str1 = armenu.split(',')
# for x in armenu:
#     ar = x.split(',')
#     menuList.append({'name': ar[0], 'price': int(ar[1])})
# f.close()
#
# for x in menuList:
#     print(x['name'], x['price'])
#

while True:
    nName = input('메뉴명 입력: ')
    if nName == '':
        break
    d = {'name': nName, 'price': int(input('가격 입력: '))}
    menulist.append(d)
for d in menulist:
    print(f"{d['name']} {d['price']}")