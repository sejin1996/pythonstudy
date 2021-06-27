# 03_if_elif3

# 사용자로부터 점수를 입력받아서 학점을 구하는 프로그램

score = eval(input("당신의 점수를 입력하세요 : "))

if score >= 90 :
    print("당신은 A 입니다.")
elif score >= 80 :
    print("당신은 B 입니다.")
elif score >= 70 :
    print("당신은 C 입니다.")
elif score >= 60 :
    print("당신은 D 입니다.")
else :
    print("당신은 F 입니다.")

