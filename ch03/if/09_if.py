# 가위바위보게임

user1_choice = input("홍길동 입력 : ")
user2_choice = input("이몽룡 입력 : ")

#
# if user1_choice == user2_choice:
#     print("비겼습니다.")
# else :
#     if user1_choice == '가위':
#         if user2_choice == '바위' :
#             print("몽룡이 이겼습니다.")
#         else :
#             print("길동이 이겼습니다.")
#     elif user1_choice == '바위':
#         if user2_choice == '보' :
#             print("몽룡이 이겼습니다.")
#         else :
#             print("길동이 이겼습니다.")
#     else :
#         if user2_choice == '가위' :
#             print("몽룡이 이겼습니다.")
#         else :
#             print("길동이 이겼습니다.")
#

######--------------------------#######

# 홍길동이 이기는 모든 경우의 수를 if 조건으로 생성
if(user1_choice == "가위" and user2_choice == "보") or (user1_choice == "바위" and user2_choice == "가위") or (user1_choice == "보" and user2_choice == "바위"):
    print("길동이 이겼습니다.")
elif user2_choice == user1_choice :
    print("비겼습니다.")
else:
    print("몽룡이 이겼습니다.")
