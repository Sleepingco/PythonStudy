# (일)정규(칙)표현식
import re


def checkemail(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    # r'\n' r은 row의 줄인말로 말그대로 날것 그대로 출력함 그러므로 줄바꿈이 아니라 '\n' 그대로 출력함
    if re.fullmatch(regex, email):
        return True
    else:
        return False


def checkmobile(mobile):
    phone_number_regex = "(\+\d{1,3})?\s?\(?\d{1,4}\)?[\s.-]?\d{3}[\s.-]?\d{4}"
    if re.fullmatch(phone_number_regex, mobile):
        return True
    else:
        return False


userId = input('Email 주소를 입력하시오')
if checkemail(userId):
    print('사용할 수 있는 이메일 입니다')
else:
    print('이메일 아이디의 형식이 틀립니다')

mobile = input('전화번호를 입력하시오')
if checkemail(userId):
    print('유효한 번호 입니다')
else:
    print('번호 형식이 틀립니다')
