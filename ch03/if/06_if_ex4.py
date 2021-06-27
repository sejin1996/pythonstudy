# o6_if_ex4

num1 = int(input("정수 1 입력 : "))
num2 = int(input("정수 2 입력 : "))
num3 = int(input("정수 3 입력 : "))



if num1 > num2 and num1 > num3:
    print("제일 큰수 : %d" % num1)
elif num2 > num1 and num2 > num3:   # num2 > num3 만으로 판별 가능
    print("제일 큰수 : %d" % num2)
elif num3 > num1 and num3 > num2:
    print("제일 큰수 : %d" % num3)
else:
    pass

