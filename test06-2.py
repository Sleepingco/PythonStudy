# import test06  # 외부모듈 가져오기 안에있는 실행문이 전부 실행됨
import pkg01.Circle as won  # 패키지 안에있는 모듈
from pkg01.Circle import around, square, volume  # 패키지 안에서 함수만 따로 호출가능

# peri = test06.around(4)
# print(f'{peri:7.2f}')

peri01 = won.around(5)
area01 = won.square(5)
volume01 = won.volume(5)
print(f'{peri01:7.2f}\n{area01:7.2f}\n{volume01:7.2f}')

peri01 = around(5)
area01 = square(5)
volume01 = volume(5)

if __name__ == '__main__':
    print(f'{peri01:7.2f}\n{area01:7.2f}\n{volume01:7.2f}')
    if peri01 is None:
        pass  # 파이썬은 조건문뒤에 실행문이 없으면 에러가 나온다 그러므로 pass를 써줘야한다 pass = donothing
    else:
        print('else')


def greeting(message='hello', times=4):
    str1 = message * times
    print(str1)


greeting('hi', 5)


def between(x):
    if 10 <= x <= 20:  # x>=10 && x<=20
        return 'between 10 and 20'
    else:
        return 'not between 10 and 20'


print(between(13))
print(between(23))
