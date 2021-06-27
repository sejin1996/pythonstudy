# 07_if_ex5

choice = int(input("도형 입력(1: 사각형, 2: 삼각형, 3 : 원) : "))
PI = 3.141592

if choice == 1 : # 사각형
    hor = eval(input("가로 입력 : "))
    ver = eval(input("세로 입력 : "))
    print(" 사각형의 면적 = %.2f" %(hor*ver))

elif choice == 2 :
    base = eval(input("밑변 입력 : "))
    h = eval(input("높이 입력 : "))
    print(" 삼각형의 면적 = %.2f" % (base * h/2))
elif choice == 3 :
    r = eval(input("반지름 입력 : "))
    print(" 원의 면적 = %.2f" % (PI*r**2))

else:
    pass

