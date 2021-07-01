# function_ret_param_ex1.py

def add(num1,num2):
    return  num1+num2

def sub(num1,num2):
    return  num1-num2

def mul(num1,num2):
    return  num1*num2

def div(num1,num2):
    return  num1/num2

a=9
b=3

print("%d + %d = %d" %(a,b,add(a,b)))
print("%d - %d = %d" %(a,b,sub(a,b)))
print("%d * %d = %d" %(a,b,mul(a,b)))
print("%d / %d = %d" %(a,b,div(a,b)))
