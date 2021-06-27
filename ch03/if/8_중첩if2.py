#8 중첩 if 2

# 사용자가 현금이나 카드를 선택하면 할인율에 따라 할인액을 계산해주고 그외를 선택하면
# 잘못입력했다고 문구를 내보낸 후 종료

num = int(input("번호 입력(1. 현금 , 2. 카드 ) : "))

if num ==1 or num ==2 :
    pay = int(input("지불액 입력 : "))
    if num == 1:
        print("할인율 : 10%")
        print("할인액 : %d" %(int(pay*0.1))+"원")
    else:
        print("할인율 : 5%")
        print("할인액 : %d" % (int(pay * 0.05)) + "원")

else:
    print("잘못입력했습니다. 종료합니다. ")
