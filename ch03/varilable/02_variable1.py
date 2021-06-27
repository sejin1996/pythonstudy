# 변수는 할당해놓고 사용하지 않으면 메모리공간을 차지하게됨
# 변수 삭제명령어 : del
# del 변수명

# c_var = 100
# print(c_var)
# del(c_var)
# print(c_var)

# 코드 블럭 주석처리 : ctrl + /

# 문자열 값 저장

# 문자열을 큰 따옴표 사용 원칙( 작은 따옴표도 사용 가능)
# 여러종류의 따움포를 사용시엔 짝을 맞춰야함

name = "홍길동"
std_name = '김철수'
pro_name = '이몽룡"교수"'

print(name)
print(std_name)
print(pro_name)

print(name, std_name, pro_name)
# 문자열을 연결하는 작업을  할때 : + 연산자 사용
address = '서울시 강남구'
print(name+"은 "+address+'에 삽니다.')

result = name + "은 "+address+"에 삽니다."
print(result)

# 문자와 숫자의 결합 (연결)
age = 23
# 값은 숫자형이지만 문자열로 처리해야 할 때는 형태를 변경함
# 숫자 -> 문자 str(변수명)
print(name + '은 ' + str(age) + "살 입니다.")

print(5+age)

# 사각형의 면적을 구해서 출력하는 프로그램
# 넓이 :100
# 높이 : 200
width = 100
height = 200

area = width * height

print("면적: " + str(area))

print("면적 : ", area)
