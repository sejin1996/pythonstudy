def var_test(a):

    a=7
    print(a,"메모리주소 : ",id(a))
    b=10
    print(b, "메모리주소 : ", id(b))

a =10
b='abc'
var_test(a)
print('전역변수a',a,"메모리주소 :",id(a))
print('전역변수b',b,"메모리주소 :",id(b))

# 매개변수의 이름을 전역변수의 이름과 같이 사용하지 말것