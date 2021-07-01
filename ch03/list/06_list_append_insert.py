# 06_list_append_insert.py
#append()

a =[1,2,3,4]

a.append(5)     #a리스트 마지막 요소로 5를 추가하고 원본 변경이 일어난다.

print(a)        #[1,2,3,4,5]

a.append([6,7])
print(a)


num=[1,2,3,4,5]
num.insert(1,200)

print(num)

# insert 함수를 이용해서 맨 뒤에 삽입 --append를 활용하는 것이 일반적
num.insert(len(num),12.3)
print(num)

num.insert(len(num)-1,[10,20])
print(num)
