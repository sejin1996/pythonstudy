# function_return_ex2.py

def get_area():
    w = int(input('가로길이 입력 : '))
    h = int(input('세로길이 입력 : '))
    return w*h

print("사각형의 면적 : %d"%get_area())
