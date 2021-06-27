# if_ex1

userID = 'flower'

UserPassword = 1234

id = input("아이디 입력 : ")
pw = eval(input("비밀번호 입력 : "))

if ((id == userID) and (pw == UserPassword)):
    print("로그인 성공!")
else:
    print("로그인 실패!")

