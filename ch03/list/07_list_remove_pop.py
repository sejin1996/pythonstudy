# 07_list_remove_pop
n = [1,2,3,3,4,5,4,3]

n.remove(4)     #4를 제거하고 원본반영

print(n)        #[1, 2, 3, 3, 5, 4, 3]

# n 리스트에서 원소값이 3인 원소를 모두 제거하시오

#3의 개수를 확인해야함
count = n.count(3)
for i in range(count):
    n.remove(3)
    print("3 삭제 ",n)

print(n)

n1= [1,1,2,1]
n1.remove(1)
n1.remove(1)
n1.remove(1)
#n1.remove(1)        ValueError: list.remove(x): x not in list
# 제거하기 전에 반드시 요소가 있는지 확인하는게 좋다

# pop() : 리스트 마지막 요소 반환하고 삭제
x =['a','b','c','d']
y=x.pop()           #'d'
print(y)            # 반환된 마지막 요소 출력
print(x)            #d 삭제된 나머지 요소만 확ㅌ에['a', 'b', 'c']

# x에 남아있는 요소 3개를 pop
x.pop()
x.pop()
x.pop()
print(x)
# x.pop() #빈 리스트에서 pop 시 에러 발생

# pop(index) : index위치에 있는 요소 반환 삭제

heros = ['슈퍼맨','스파이더맨','헐크','아이언맨']
temp = heros.pop(2)
print(temp)
print(heros)