# function_return_ex3.py

def order():
    price = int(input("상품가격 입력 : "))
    amount = int(input("주문수량 입력 : "))
    return price,amount,price*amount

p,a,t = order()

print("---------------------------")
print("상품가격 : %d 원" %p)
print("주문수량 : %d 개" %a)
print("주문액 : %d 원" %t)
