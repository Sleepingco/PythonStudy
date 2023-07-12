# create
arName = [1, 'hello', 3.14, True, None, 'world']

arName.append(25)
arName.insert(3,'박성호')

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
arName[3] = '하이미디어'

# delete
arName.remove(3.14)
arName.remove('하이미디어')
del arName[3]
for i in arName:
    print(i)
print('-'*30)
for i in range(len(arName)):
    print(i, '=', arName[i])


