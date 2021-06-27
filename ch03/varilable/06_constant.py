# 06_constant.py
# 값이 변경되지 않는 값
# 파이썬에서는 별도의 상수가 없음
# 변수와 구분하기위해 대소문자로 사용할 뿐
# 나중에 상수의 값을 변경해도 오류없음

PI = 3.141592
r = 10

area = r * r * PI

print(area)

INT_RATE = 0.03

deposit = 10000

interest = deposit * INT_RATE
balance = deposit + interest

print(balance)
print(int(balance))  # int() 정수변환형 함수

# 천단위 구분기호

print(format(int(balance), ','))  # format(출력값, 구분기호)

INT_RATE = '이자율' # 값을 변경해도 오류발생하지 않음


