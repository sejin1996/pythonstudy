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

print("==enumerate==")
# enumerate(iterable,start=0)
# 시퀀스 형태의 값을 넘겨주면 index값을 포함하는 enumerate객체로 반환 해 주는 함수
# (리스트, 튜플, 문자열, range) => 인덱스 값, 실제값

# ['a', 'b', 'c'] => 0'a' 1'b' 2'c'

# <enumerate object at 0x0000017F5D2BBB80>
print(enumerate(["kim",'lee',"Park"]))


for i, name in enumerate(["kim",'lee',"Park"]):
    print(i,name)

# index와 값을 나타내는 변수명은 임의로 사용가능
# for문처럼 반복되는 구간에서
# 객체가 현재 어느위치에 있는지 알려주는 인덱스 값이 필요할때 enumerate함수를 사용하면 매우유용

print('===eval====')
# eval(expression) : 표현식의 연산결과 반환

print(type(eval('10')))

print(type(eval('10.5')))

print(eval('1+2'))  # 수식을 표현한 문자열을 실제식으로 변환 후 연산결과를 반환

print("=======filter()=======")
# filter(function 이름, iterable)j : 반복가능한 자료형 요소들이
# function에 입력되었을 때 반환값이 참인것만 묶어서 (걸러내서) 반환

# 양수만 반환하는 함수

def positive(x):
    return x>0  # 함수 반환 결과가 True/False

print(filter(positive,[0,-1,4,-7,10]))   #<filter object at 0x0000026F8931E850>
print(list(filter(positive,[0,-1,4,-7,10])))    # [4,10]

# 짝수만 반환
def even_number(x):
    if x%2 ==0:
        return x

print(list(filter(even_number,[0,1,2,3,4,5,6,7,8,9,10])))

print("====help()=====")
# 내장 도움말 시스템을 호출
help(print)
help(sum)

print("===hex()====")

# hex() : 정수를 "0x"접두사가 붙은 소문자 16진수 문자들로 반환

print(hex(8))
print((hex(35)))
print((hex(1234)))

print('=====map=====')
# map(function이름, iterable) : iterable 각 요소가 함수 function에 의해 수행된 결과 반환

def increase(x):
    return x+1

print(map(increase,[1,2,3,4,5]))            # <map object at 0x0000021441FEE760>
print(list(map(increase,[1,2,3,4,5])))      # [2, 3, 4, 5, 6]

print("==open()=======")
# 외부 파일을 사용하기위해 접근경로를 생성하는 함수(파일이 없으면 만들고, 있으면 해당파일을 열어준다)
file_write = open('my_file.txt','w')

print("===round()====")

# 실수를 반올림하여 반환
# round(number,[,ndigits]) : ndigit - 소수 이하 자리수

print(round(3.141592,3))        # 3.142

print("===zip()======")

# zip(iterable, iterable1....) : 각 iterable 에서 동일한 인덱스의 요소를 추출하여 튜플형태로 묶어서 반환

print(zip([1,2,3],[4,5,6],[7,8,9]))
print(list(zip([1,2,3],[4,5,6],[7,8,9])))
print(list(zip([1,2,3],[4,5])))

print(list(zip('123','abc'))) #[('1', 'a'), ('2', 'b'), ('3', 'c')]

# zip 함수를 사용해서 튜플로 부터 딕셔너리를 생성하는 예제

keys = ('apple', 'pear','peach')
vals =(300,250,400)

result = dict(zip(keys,vals))
print(result)                   # {'apple': 300, 'pear': 250, 'peach': 400}
