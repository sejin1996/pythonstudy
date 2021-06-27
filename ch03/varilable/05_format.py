# print(파라미터) : 화면의 결과를 출력

# print(x) : x 변수의 값을 화면에 출력

# print()함수를 이용해서 문자열과 변수의 값을 함께 출력하고 싶을때

# print("문자열", 변수명) - 방법1 => 문자열을 먼저 출력하고 변수명을 출력

age = 25

print("내나이는", age)

print("내 나이는"+str(age)+ "입니다")

kor = 90
eng = 80
math =80

total = kor+eng+math
average = total/3

print("총점: %d, 평균 : %.2f" % (total, average))
