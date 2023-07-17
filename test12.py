class Menu:
  def __init__(self, filepath):  # 생성자
    self.menulist = []  # [{}, {}, {}]
    self.filename = filepath
    self.build()

  def build(self):  # self는 선언할때만써야함
    # f = open('c:/temp/menu1.txt', 'r')
    f = open(self.filename, 'r')
    armenu = f.readlines()
    # arMenu = ['Latte,3000','Mocca,3500','Americano,2500','Cappuccino,3600']
    # 반복해서 arMenu의 값(원소/요소)을 읽어서 split한후, self.menuList에 딕셔너리로 구성하여 저장.
    for x in armenu:
      ar = x.split(',')
      self.menulist.append({'name': ar[0], 'price': int(ar[1])})
    f.close()

  def save(self):
    f = open('c:/temp/menu1.txt', 'w')
    newline = ''
    for i in self.menulist:
      f.write(f"{i['name']},{i['price']}")
      # line = newline + f"{i['name']},{i['price']}" 위에 코드랑 같은뜻
      # f.write(line)
      newline = '\n'
    f.close()

  def display(self):
    n = 1
    for x in self.menulist:
      print(f"{n:2d}.{x['name']:12s}, {x['price']:5d}")
      n += 1

  def add(self):
    while True:
      nName = input('메뉴명 입력: ')
      if nName == '':
        break
      self.menulist.append({'name': nName, 'price': int(input('가격 입력: '))})
      self.display()
    self.save()
  def update(self):
      # self.display()
      # 수정할 메뉴번호 읽어 들이기
      # 메뉴 번호가 빈 문자열이 아닌동안
      # 메뉴명읽기
      # 가격 읽기
      # 해당번호의 메뉴명, 가격
      # update list[0] = {'name': nName, 'price': int(input('가격 입력: '))}
      # self.display()
      # 수정할 메뉴번호 읽어 들이기
      # self.display()
    while True:
      ndx = int(input("메뉴번호 입력 ['':종료]"))
      if ndx == '':
        break
      nName = input('새메뉴명 입력: ')
      nPrice = int(input('새가격 입력: '))
      ndx = int(ndx)-1
      self.menulist[ndx] = {'name': nName, 'price': nPrice}
      self.display()
    self.save()
  def delete(self):
    # 지울 메뉴번호 읽어들이기
    # 메뉴번호가 빈 문자열이 아닌 동안,
    # del self.menulist[n]
    # self.display()
    # self.save()
    while True:
      ndx = input('지울 메뉴번호 입력: ')
      if ndx == '':
        break
      ndx = int(ndx)-1
      if 0 <= ndx < len(self.menulist):
        del self.menulist[ndx]
        self.display()
      else:
        print('잘못된 메뉴번호입니다.')
      self.save()
