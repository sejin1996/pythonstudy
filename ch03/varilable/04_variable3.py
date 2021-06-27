# 화씨 온도를 섭씨 온도로 변환

fTemp = 90 #정수 변수

cTemp = (fTemp - 32)*5/9 #정수 연산

print(cTemp)

print("%f"%cTemp)
print("%.3f"%cTemp)
print("%10.3f"%cTemp)

# 실수 %f 사용시 실수 전체자리수. 소수자리 수f

print("화씨온도 %d를 섭씨온도로 변환하면 %.3f 입니다" % (fTemp, cTemp))


