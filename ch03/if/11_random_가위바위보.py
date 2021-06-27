# 11_random_가위바위보
# 홍길동과 컴퓨터간의 가위바위보

# 랜덤 모듈 가져오기
from random import randint

# 난수 발생: 1 : 가위 , 2 : 바위 , 3 : 보


n = randint(1,3)

if n == 1:
    user2_choice = '가위'
elif n == 2:
    user2_choice = '바위'
else:
    user2_choice = '보'


user1_choice = input("홍길동 입력 : ")
# 홍길동이 이기는 모든 경우의 수를 if 조건으로 생성
if(user1_choice == "가위" and user2_choice == "보") or (user1_choice == "바위" and user2_choice == "가위") or (user1_choice == "보" and user2_choice == "바위"):
    print("길동이 이겼습니다.")
elif user2_choice == user1_choice :
    print("비겼습니다.")
else:
    print("컴퓨터가 이겼습니다.")
