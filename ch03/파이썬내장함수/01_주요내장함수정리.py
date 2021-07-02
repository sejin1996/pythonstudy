# 01_주요내장함수정리

# 내장함수

# abs(x) : x 의 절대값을 반환
print(abs(-10))

print(("==all()=="))
# all(iterable) : 모든 요소가 참이면 True, 아니면 False 반환
# False : 0 , True : 0 이 아닌 모든 값
# 즉 0 이 하나라도 있으면 False 반환
# iterable:각각의 요소를 하나씩 반환할 수 있는 객체/for 문으로 반복해서 출력이 가능한 자료형
# 리스트,튜플,집합,딕셔너리

print(all([1,2,3]))
print(all([0,1,2,3,4]))

print("==any()==")
#any(iterable) : 하나라도 참이면 True, 모두 거짓이면 False
# 전부 0이면 False, 아니면 True
print(any([0,0,0]))
print(any([0,1,0]))
print(any([0,"",[]]))   # 0,빈문자열,빈리스트 - False

print("==chr()==")

#chr(i) : 아스키(ASCII)코드 값에 해당하는 문자 반환

print(chr(65))      # A
print(chr(97))      # a
print(chr(13))      # enter

for i in range(65,100):
    print(chr(i),end=" ")

print("==ord()==")

#ord(c) : chr 과 반대로 문자에 해당되는 아스키 코드 값을 반환

print(ord('a'))     #97
print(ord('0'))     #48
print(ord('\n'))    #10
print(ord(" "))     #32 : 스페이스
print(ord('\r'))    #13 : enter

print("====divmod()===")
# divmod(a,b) : a를 b로 나눈 몫과 나머지를 튜플 형태로 반환
print(divmod(7,3))



