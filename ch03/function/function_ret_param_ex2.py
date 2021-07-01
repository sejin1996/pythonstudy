# function_ret_param_ex2.py

def get_interest(diposit,int_rate):
    return diposit*int_rate/100

diposit = int(input("예금액 입력 : "))
int_rate= float(input("이자율 입력(%) : "))
interest=get_interest(diposit,int_rate)
print("이자액 : %d 원"%int(interest))

