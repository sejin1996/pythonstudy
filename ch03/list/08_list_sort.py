# 08_list_sort.py

# sort() : 리스트 정렬, 원본 리스트 변경
scores = [90,78,81,64,89]; print()
scores.sort()       # 기본 : 오름차순 정렬
print(scores)       # [64, 78, 81, 89, 90]

scores = [90,78,81,64,89]; print()
scores.sort(reverse=True)   # 내림 차순 정렬
print(scores)

scores = [90,78,81,64,89]; print()
scores.reverse()            # 원소의 위치를 역순으로 변경( 정렬은 안함)
print(scores)               # [89, 64, 81, 78, 90]

## 문자의 정렬       --  대문자 < 소문자 , A~Z , a~z

char = ['b','A', 'd','C']
char.sort()
print(char)                 # ['A', 'C', 'b', 'd']

#대소문자 구별없이 정렬
# key = str.lower

char = ['b','A', 'd','C']
char.sort(key=str.lower)
print(char)
# 대소문자 구별없이 내림차순정렬
char = ['b','A', 'd','C']
char.sort(key=str.lower,reverse=True)
print(char)                 # ['d', 'C', 'b', 'A']

# 문자열은 첫 문자로 정렬됨
ids = ['SKY','Blue','red','eBook','GREEN']
ids.sort(key=str.lower)         # 오름차순으로 정리
print(ids)                      # ['Blue', 'eBook', 'GREEN', 'red', 'SKY']