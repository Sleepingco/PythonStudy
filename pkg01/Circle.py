import math# 파이썬 기본 제공 모듈
# around = lambda r: 2*math.pi*r  # 둘레
# square = lambda r: math.pi*r**2  # 넓이
# volume = lambda r: 4/3*math.pi*r**3  # 체적,부피

def around(r=4): # 함수에 디폴트값을 줄 수 있다
    return 2*math.pi*r
def square(r=4):
    return math.pi*r**2
def volume(r=4):
    return 4/3*math.pi*r**3

if __name__ == '__main__': # 메인모듈로서 작동될때만 실행한다
    radius = float(input('반지름[단위:m]'))
    if radius != '':
        radius = float(radius)
        print('둘레 ', around(radius), '\n면적 ', square(radius), '\n체적', volume(radius))
    else:
        print('둘레 ', around(), '\n면적 ', square(), '\n체적', volume())
    if radius == '':
        radius = float(radius)
        print('둘레 ', around(radius), '\n면적 ', square(radius), '\n체적', volume(radius))
    else:
        print('둘레 ', around(), '\n면적 ', square(), '\n체적', volume())