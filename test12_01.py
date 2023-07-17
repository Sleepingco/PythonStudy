import test12
import test12_02
import test12_03
menufile = 'c:/temp/menu1.txt'
menu = test12.Menu(menufile)
sale = test12_03.Sale()

menu.display()
# 작업선택(M:메뉴관리, O:주문관리, S:매출관리, ''/X:종료
while True:

  command = input("M:메뉴관리,O:주문관리,S:매출관리, ''/X:종료 :")
  if command.lower() == 'x' or command == '':
    break
  elif command .lower()== 'm':
    while True:
      order = input('추가:C 목록보기:R 수정:U 삭제:D 종료:''/X')
      if order == '' or order.lower() == 'x':
        break
      elif order.lower() == 'c':
        menu.add()
      elif order.lower() == 'r':
        menu.display()
      elif order.lower() == 'u':
        menu.update()
      elif order.lower() == 'd':
        menu.delete()
      else:
        print('잘못된 명령어 입니다')
  elif command.lower() == 'o':
    nOrder = test12_02.Order(menufile)
    while True:
      order = input("주문하기:A 주문내역보기:R 주문취소:D 주문관리종료:''/x")
      if order.lower() == 'a':
        # a : 주문받기 r: 보여주기 d: 주문삭제
        nOrder.add()
      elif order.lower() == 'r':
        nOrder.orderdisplay()
      elif order.lower() == 'd':
        nOrder.orderdelete()
      elif order.lower() == 'x' or order == '':
        break
      else:
        print('잘못된 명령어 입니다')
      # orderList의 길이가  0과같으면,그냥종료
      # 그렇지 않으면 sales.add(mobile, order.orderList)
    if len(nOrder.orderList) > 0:
      mobile = input('전화번호 입력')
      for x in nOrder.orderList:
        lorder = [x]nOrder.orderList
      sale.add(mobile, lorder)
    else:
      break
  elif command.lower() == 's':
    # 매출보기
    sale.display()
  else:
    print('잘못된 명령어 입니다')
