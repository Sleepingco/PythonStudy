import test12
menu = test12.Menu()
while True:
  order = input('명령어 c,r,u,d 중 입력')
  if order == '':
    break
  elif order == 'c':
    menu.add()
  elif order == 'r':
    menu.display()
  elif order == 'u':
    menu.update()
  elif order == 'd':
    menu.delete()
  else: print('잘못된 명령어 입니다')