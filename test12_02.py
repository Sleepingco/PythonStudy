import test12
class Order(test12.Menu):
    def __init__(self, filepath):
        # orderList안에 들어가는 딕셔너리는 세가지 정보를 포함한다
        # 메뉴명 수량 총액
        super().__init__(filepath)
        self.orderList = []

    def add(self):
        # 메뉴 목록을 보여준다
        # 주문할 메뉴 번호를 입력받는다('':종료)
        # 수량을 입력받는다
        # 총액을 계산/표시
        # orderList에 추가
        super().display()
        # orderNum=1
        while True:
            ondx = input("주문할 메뉴번호를 입력해주세요 ['':종료]: ")
            if ondx == '':
                break
            ondx = int(ondx)-1
            qty = int(input('주문할 메뉴의 수량을 입력해주세요: '))
            total = self.menulist[ondx]['price'] * qty
            if 0 <= ondx < len(self.menulist):
                o = self.menulist[ondx]
                self.orderList.append({'menu': o['name'], 'qty': qty, 'total': total})
                self.orderdisplay()
            else:
                print('잘못된 메뉴번호입니다.')


            # super().display()
            # num  = input('주문')
            # if num =='': brak
            # num = int (num)-1
            # name  = self.menulist[num]['name']
            # price = self.menulist[num]['price']
            # qty = int(input('수랑'))
            # self.orderList.append({'onme':orderNum,'name':name,'qty':qty})
            # orderNum+=1
    def orderdisplay(self):
        # 주문내역을 보여준다
        n = 1
        for x in self.orderList:
            print(f"주문번호{n:2d}.{x['menu']:12s},수량{x['qty']:2d}, 가격{x['total']:7d}")
            n += 1

    def orderdelete(self):
        # 메뉴목를을 보여준다
        # 삭제한 주문번호를 입력받는다('':종료)
        # orderLsit에서 삭제 (주문번호 -1해야 지울 주문의 인덱스가 구해짐)
        self.orderdisplay()
        while True:
            dndx = input("취소할 메뉴번호를 입력해주세요 ['':종료]: ")
            if dndx == '':
                break
            dndx = int(dndx) - 1
            if 0 <= dndx < len(self.menulist):
                del self.orderList[dndx]
                self.orderdisplay()
            else:
                print('잘못된 메뉴번호입니다.')
