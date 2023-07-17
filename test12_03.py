class Sale:
    def __init__(self):
        # sales list 는 모바일 번호 메뉴명 수량  총액
        self.sales = []

    def add(self, number, order):
        # 모바일번호를 입력받는다
        # add orderlist to salseList
        self.sales.append({'phone': number, 'order': order})
        print(self.sales)

    def display(self):
        # 매출내역 출력
        # 매출총액 표시
        pass
