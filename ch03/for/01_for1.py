# 01_for1
# for 문 : 정해진 횟수만큼 반복할 때 주로 사용
# 문법
# for (반복 요소를 저장할 변수) in (반복을 위한 리스트 또는 범위) :
#     반복문장1
#     반복문장2

# 리스트["홍길동","이몽룡","성춘향","변학도"]의 요소를 모두 출력하시오

s_name =["홍길동","이몽룡","성춘향","변학도"] #list 생성

# print(s_name[0])
# print(s_name[1])
# print(s_name[2])
# print(s_name[3])

for name in s_name :
    print(name)

# #-----
# 반복범위 설정 : range()함수
# 특정범위의 정수생성
# range(start,stop,step)
print()
print("==========================")

# range(10) # start, step 생략 10개의 정수 0~9 까지의 정수 (시작은 0)

for i in range(10) : # 0~9
    print(i)
print("=========")
# range(1,10) #  step 생략 1에서 9 까지 정수 - start에서 stop-1 까지의 정수

for i in range(1,10) : # 1~9
    print(i)
print("=========")
# range(1,10,2) #  start에서 stop-1 까지 step 만큼 건너뛴 정수

for i in range(1,10,2) : #
    print(i)

















