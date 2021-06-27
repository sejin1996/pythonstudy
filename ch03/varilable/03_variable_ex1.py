name, no, year, grade, average = "홍길동", 2016001, 4, 'A', 93.5
level = 10
print("성명 : "+name)
print("학번 : "+str(no))
print("학년 : "+str(year))
print("학점 : "+grade)
print("평균 : "+str(average))

# 포멧코드 사용
# 문자열 : %s
# 정수 : %d
# 실수 : %f
# 문자하나 : %c
print("성명 : %s" % name)
print("학번 : %d" % no)
print("학년 : %d" % year)
print("학점 : %c" % grade)
print("평균 : %.2f" % average)
print("등급 : %d%%"%level) # 등급 : 10% 출력하고 싶음 -- %문자 출력하고 싶으면 %%

