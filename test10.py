pid = input('주민번호를 입력하시오')
n = 2
sum = 0
str1 = ''
for i in pid[:-1]:
  sum += int(i) * n
  if str1 != '':
    str1 += '+'
  str1 += i + 'x' + str(n)
  n += 1
  if n > 9:
    n = 2
print(11 - sum % 11, ',', pid[-1])
print(str1)
