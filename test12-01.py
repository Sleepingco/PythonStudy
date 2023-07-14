import test12

menu = test12.Menu()
# 작업선택(M:메뉴관리, O:주문관리, S:매출관리, ''/X:종료
while True:
  command = input('M:메뉴관리,O:주문관리,S:매출관리, ''/X:종료')
  if command == 'x' or '':
    break
  elif command == 'm':
    while True:
      order = input('추가:C 목록보기:R 수정:U 삭제:D 종료:''/X')
      if order == 'x' or '':
        break
      elif order == 'c':
        menu.add()
      elif order == 'r':
        menu.display()
      elif order == 'u':
        menu.update()
      elif order == 'd':
        menu.delete()
      else:
        print('잘못된 명령어 입니다')
  elif command == 'o':
    while True:
      order = input("주문하기:O 주문내역보기:R 주문관리종료:''")
      if order == 'o':
        pass
      elif order == 'r':
        pass
      elif order == 'x' or '':
        break
  elif command == 's':
    # 매출보기
    pass
  else:
    print('잘못된 명령어 입니다')
