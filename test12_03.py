class Sale:
    def __init__(self):
        # sales list 는 모바일 번호 메뉴명 수량  총액
        self.sales = []

    def add(self, order):
        # 모바일번호를 입력받는다
        # add orderlist to salseList
        if len(order) < 1:
            return
        mobile = input("전화번호 입력('-')['':기본값으로입력]")
        if mobile == '':
            mobile = '-'
        for x in order:
          d = ({'phone': mobile, 'name': x['name'], 'qty': x['qty'], 'sum': x['sum']})
          self.sales.append(d)

    def display(self):
        # 매출내역 출력
        # 매출총액 표시
        total = 0
        for d in self.sales:
            print(d)
            total += d['sum']
        print('매출총액: ' + str(total)+'원')
