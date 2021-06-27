#정수 2개를 입력받아서 두수 사이의 합을 구하는 프로그램 작성

num1 = int(input("숫자1 입력 : "))
num2 = int(input("숫자2 입력 : "))

sum = 0
for x in range(num1,num2+1):
    sum += x
print("%d부터 %d 까지의 합 : %d"%(num1,num2,sum))
