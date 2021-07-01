# find_index_ex

# 입력된이메일의 형식 확인하는 프로그램
# 이메일 형식이아닌경우

# @ 없는경우
# .없는 경우
# @와.사이에 문자가 없는경우
# @와 . 사이에 문자가 없는 경우
# @앞에 문자가없는경우
# .뒤에 문자가 없는 경우
# @두번 이상 있는 경우
# .두번 이상 있는 경우
email = input("이메일 입력 : ")

if(
    email.find("@")==-1 or                      # @없는 경우
    email.find(".")==-1 or                      # .없는 경우
    email.index("@")>email.index(".")or         # @와.사이에 문자가 없는경우
    email.index(".")-email.index("@") < 2 or    # @와 . 사이에 문자가 없는 경우
    email.index('@')==0 or                       # @앞에 문자가없는경우
    len(email)-email.index(".") <= 1 or         # .뒤에 문자가 없는 경우
    email.count("@") >= 2 or                    # @두번 이상 있는 경우
    email.count(".") >= 2                       # . 2번 이상 있는 경우

):
    print("이메일 형식이 아닙니다.")

print("입력한 이메일 : ", email)

