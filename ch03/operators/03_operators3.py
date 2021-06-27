# 03_operators3

# 현금이 5000원이 있고 사탕가격이 120원인경우 최대 살수있는 사탕개수와 나머지돈은?

myMoney = 5000

candyPrice = 120

#최대한 살수 있는 사탕개수

candies = myMoney // candyPrice

# 사탕을 구입하고 남은돈

change = myMoney % candyPrice

print("사탕 %d 개를 사고 남은돈 : %d 원" % (candies, change))

