# function_gbb_game.py
from random import randint
def gbb_game():
    com =randint(1,3)
    you = int(input("YOU 입력 (1:가위 ,2:바위, 3:보 ) : "))
    if (you ==1 and com ==3 )or (you ==2 and com ==1 )or(you ==3 and com ==2 ):
        print("당신이 이겻습니다.")
        print("com : %d"%com)
    elif (you ==1 and com ==1 )or (you ==2 and com ==2 )or(you ==3 and com ==3 ):
        print("비겼습니다.")
        print("com : %d" % com)
    elif (you ==1 and com ==2 )or (you ==2 and com ==3 )or(you ==3 and com ==1 ):
        print("컴퓨터가 이겼습니다.")
        print("com : %d" % com)
    else:
        print("잘못 입력했습니다.")


gbb_game()