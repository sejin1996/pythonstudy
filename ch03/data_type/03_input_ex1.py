# 03_input_ex1.py

kor = eval(input("국어 점수 입력 : "))
en = eval(input("영어 점수 입력 : "))
Math = eval(input("수학 점수 입력 : "))

total = kor + en + Math

average = total/3

print("총점 : ", total)
print("평균 : %.2f" % average)

