# 02_while_3의 배수의 합
#
# 1부터 100사이의 모든 3의 배수의 합을 while문을 이용해서 코드 작성
# 누적변수

sum_v = 0

# 초기값
num = 1

while num <= 100 :
    # num 이 3의 배수인지 확인
    if num % 3 == 0 :
        sum_v += num
    num += 1

print("1~100까지의 모든 3의 배수의 합은 %d입니다."%sum_v)

#최종num의 값은얼마인가?

print("반복후 num의 값은 %d 입니다" %num)