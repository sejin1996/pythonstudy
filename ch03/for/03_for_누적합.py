# 03_for_누적합
# 1부터 10까지 출력하고 1~10 까지 더한 결과 프로그램을 작성하시오

sum = 0         # 누적 변수는 사용하기 전에 반드시 선언해야함

for x in range(1, 11) :
    print(x)
    sum += x

print("1부터 10까지 누적합", sum)

## 1부터 100까지 더하는 프로그램을 작성하세요
sum = 0
for x in range(1, 101) :

    sum += x

print("1부터 100까지 누적합", sum)