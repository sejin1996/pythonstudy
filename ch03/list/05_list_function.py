# 05_list_function

print("===========================")

# append():리스트의 끝에 새로운 요소 추가
# 리스트.append(새로 추가할 요소)
#
# insert():리스트의 특정 위치에 요소 삽입
# 리스트.insert(삽입위치, 새로추가할 요소)

# 06_list_append_insert.py 에 정리

# remove() : 리스트에서 값에 해당되는 요소 제거
# 리스트.remove(제거할 요소값)
# 동일한 값이 여러개 있는 경우 첫번쨰 값만 제거
# 동일한 값 모두를 제거하려면 for 문을 사용

# pop() : 리스트의 마지막 요소 반환하고 삭제
# 리스트.pop()
# 인덱스 위치에 있는 요소 반환 삭제
# 리스트.pop(인덱스값)

#extend()
# 리스트의 확장
# 리스트.extend()
# 이전 리스트에 원소 추가하여 확장된 리스트로 됨
# 원래 리스트 변경됨

a=[1,2,3]
a.extend([4,5])

print("a리스트 :",a)
# a리스트 : [1, 2, 3, 4, 5]

b=[1,2,3]
b.append([4,5])
print("b리스트 :",b)
# b리스트: [1, 2, 3, [4, 5]]

c=[1,2,3]
c.insert(len(c),[4,5])
print("c리스트 :",c)
# c리스트 : [1, 2, 3, [4, 5]]

# sort()/reversed()/sorted(): 원소의 정렬과 관련된 함수

#index ()
# 리스트 안에서 원소의 위치 값 반환
a=[1,2,3,4,5,5]
print(a.index(2))        #a[1] 번째 위치 반환
print(a.index(1))
print(a.index(5))

# min() : 리스트 내에서 최소값 원소 반환
# max() : 리스트 내에서 최대값 원소 반환

n=[100,7,-2,99,30]

print(max(n))
print(min(n))

# min, max 함수는 char / str  지원하지 않는다.

# in / not in (포함 여부 판단 후 True/False로 반환)
num = [1,2,3,4,5]
result = 2 in num       # 2가 있니?
print(result) # True

result = 2 not in num       # 2가 있니?
print(result) # False

# 리스트 일치 검사
# # 비교 연산자를 사용해서 2개의 리스트 비교 (==, !=, >,>=.<=,<)
# 첫번째 요소부터 비교 시작
# 첫번째 요소의 비교에서 결과가 False  면 더이상 비교하지 않고 첫번쨰 요소가 동일하면 두번째 요소 비교
# 리스트 안의 모든 요소 비교 결과가 True 면 전체결과 True

list1=[5,2,3]
list2=[1,2,3]

print(list1>=list2)