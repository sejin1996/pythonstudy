# 정수
a = 0b1011      # 2진수
b = 300         # 10진수
c = 0o123       # 8진수
d = 0x12fc      # 16진수


print(a, b, c, d)   # print()는 10진수로 표현

# 실수
f = 3.14

f1 = -1234.45

f2 = 1.234567e5

print(f, f1, f2)

# 문자열

char1 = 'A'
char2 = 'B'

print(char1, char2)

str1 = '홍길동'
str2 = "python"
str3 = """python Programming"""
str4 = '''파이썬 프로그래밍'''
str5 = """여러줄로 
나누어서
출력가능 """

print(str5)

# 논리값/특수 리터럴

t = True
f = False

print(t, f)

val = None
val1 = ''

print(type(val), type(val1))

# 한줄의 코드를 여러줄에 나눠서 표현 역슬래시 (\)또는 괄호() 사용

a = 1+2+3+\
    4+5+6

b = (1+2+3+
     4+5+6)

print(a, b)



#####################
# print 함수를 이용해서 문자열을 출력하고자 할 때 여러행 입력

print("긴문장을 입력할 때 중간에서 엔터키를 치면"
      "다음행으로 가고 자동으로 따옴표 처리되면서 "
      "1줄로 인식되고 한줄로 출력")

print("긴문장을 입력할 때 중간에서 엔터키를 치면\n"
      "다음행으로 가고 자동으로 따옴표 처리되면서 \n"
      "1줄로 인식되고 한줄로 출력")

#세미콜론(;)을 이용하여 한행에 입력 가능

print("한줄에") ; print("두개의 명령어")


