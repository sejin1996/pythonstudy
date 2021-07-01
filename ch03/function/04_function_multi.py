# 04_function_multi

# 여러개의 값 반환하기
# 파이썬을 제외한 다른 프로그램 언어에서 함수는 항상 하나의 값만 반환
# 파이썬에서는 함수가 여러개의 값을 반환할 수 있음

def multi_return():
    return 1,2,3
    # return 1      1은 반환하고 2,3은 반환되지 않음
    # return 2      코드는 존재
    # return 3

a,b,c = multi_return()  #반환된 여러개의 값을 변수에 저장 -> 여러변수에 저장해야함
print("여러 변수에 저장 후 출력")
print(a,b,c)

print("반환된 값을 바로 출력")
print(multi_return())
print(type(multi_return()))

