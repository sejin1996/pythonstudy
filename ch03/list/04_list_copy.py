a=[1,2,3]

# a 리스트의 값을 변수 b에 복사하시오 (저장하시오)

b = a

print(a)
print(b)

b[0] =100
print(a)
print(b) # 주소값만 참조한것이기 때문에 b[0]만 변경하더라도 a[0]의 원소값도 변경된다.

# 깊은복사(deep copy)
# list()함수 또는 deep copy()함수를 사용해서
# 리스트의 복사본을 새로생성하여 반환
# 복사본 리스트 원소의 값을 변경하여도 원본 리스트 원소의 값은 변경되지 않음

scores = [1,2,3,4,5]
values = list(scores)

print(scores)
print(values)

values[0] = 100

print("scores : ",scores)
print("values : ",values)

# deepcopy()함수 : 깊은 복사
# copy모듈을 import해야함

import copy

a = ['a','b','c']
b=copy.deepcopy(a)


print("b 리스트 수정전")
print(a)
print(b)
b[0]=1

print("b 리스트 수정전")
print(a)
print(b)