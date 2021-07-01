# 07_function_param
# 인수(인자) 와 매개변수 정리
# 인수(인자) : argument

# 함수에게 실제로 전달되는 값 (호출할 때 전달하는 값)
# print("hello") - "hello" => 인자

# 매개변수 (parameter)
# 함수를 호출할 떄 전달되는 실제 값을 받아 저장하는 변수
# def print(data)

def show_name(name):
    print(name)

# show_name 호출

# show_name() #매개변수를 사용하지 않은 경우 {TypeError: show_name() missing 1 required positional argument: 'name'}
# show_name("홍길동")
show_name(123)  # 매개변수도 인자값에 의해 결정된다.