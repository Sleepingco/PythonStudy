# i = int(input('i값을 넣으시오'))
# j = int(input('j값을 넣으시오'))
# if j == 0:
#     print('불능')
# else:
#     print(i / j)

try:
    i = int(input('i값을 넣으시오'))
    j = int(input('j값을 넣으시오'))
    if j == 0:
        raise ZeroDivisionError(i, j)
    print(i / j)
except ZeroDivisionError as e:  # 사용한 메모리정리
    print('불능', e.args)
except ValueError:
    print('입력된 값의 형태가 적절하지 않습니다')
except:  # 모드 에러를 받는다
    print('예외처리 완료')
