# 05_input_ex3

deposit = eval(input("예금액 입력 : "))
YTM = eval(input("이자율 입력(%) : "))

interest = deposit * (YTM/100)
balance = deposit + interest
print("---------------------------------")
print("예금액 : %d 원" % deposit)
print("이자율 : %.1f %%" % YTM)
print("예금이자 : %d 원" % interest)
print("잔액 : %d 원" % balance)
print("---------------------------------")

print("예금액 : ", format(deposit, ','), '원')
print("이자율 : ", YTM, '%')
print("예금이자 : ", format(int(interest), ','), '원')
print("잔액 : ", format(int(balance), ','), '원')
