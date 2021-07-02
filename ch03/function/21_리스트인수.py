# 21_리스트인수

# 리스트를 함수에 인수로 전달 할 때
def show_list(func_list):
    func_list[0]=10
    print(func_list)
    print("1,func_list id : ",id(func_list))    #리스트 요소 하나만 변경할떈 주소 변경되지 않음
    func_list=[10,20,30,40]
    print(func_list)
    print("2.전체 변경후 func_list id :",id(func_list))  # 새로운 변수를 생성 -주소공간도 달라지게 된다.


my_list=[1,2,3,4]
show_list(my_list)
print(my_list)          # 원본도 변경되게 된다.
print(id(my_list))

# 함수 인수를 변수로 사용하면 값이 전달되는 게 아니고, 참조 주소가 전달되면서 같은 메모리를 참조하게 된다.
# 일반 변수는 전달된 매개변수에 값을 변경하면 메모리 주소가 달라지면서 다른 변수로 생성
# 리스트 변수는 전달된 매개 변수의 일부값을 변경하면 원본도 변경시키고, 전체를 변경하면 메모리 주소가 달라지게 된다.
# 지역변수 전역변수 이름 다르게 생성하는 것을 권장.
