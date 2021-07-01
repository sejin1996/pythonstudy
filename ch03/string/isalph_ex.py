# isalph_ex

# count 누적변수 초기화
alphas =digits=spaces=others=0

string = input("문장을 입력하세요 : ")

for c in string:
    print(c)        #c 변수에 한문자씩 대입
    if c.isalpha(): # 문자라고 판단되면 c.isalpha() == true
        alphas = alphas + 1
    elif c.isdigit():
        digits += 1
    elif c.isspace():
        spaces += 1
    else:
        others += 1

print("문자 : %d 개"%alphas)
print("숫자 : %d 개"%digits)
print("띄어쓰기 : %d 개"%spaces)
print("그외 : %d 개"%others)

