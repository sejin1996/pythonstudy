# 02_exception1.py
# 예외처리 예제

# 에러종류와 상관없이 모든 에러 처리
# try~except 구문

# try :
#     # print(10/0)     # 에러가 발생하면 무조건
#     print("나이 :"+23+"살")
# except:             # 본 구문으로 포커스 넘어옴
#     print("오류 발생! ")
#
# print('============Exception 클래스 사용==========')
#
#
# try :
#     # print(10/0)     # 에러가 발생하면 무조건
#     print("나이 :"+23+"살")
# except Exception:             # 본 구문으로 포커스 넘어옴
#     print("오류 발생! ")

# 에러 종류 명시
# try :
#     print("나이 :" + 23 + "살")  # Type Error 발생   - 에러발생 이후 문장은 실행하지 않는다.
#     print(10/0)    # ZeroDivisionError 발생 - 바로 except 구문으로 분기
#     print("나이 :" + 23 + "살")  # Type Error 발생
# except ZeroDivisionError:         # 0으로 나눈 논리에러만 처리 위코드의 type 에러는 처리하지 않는다
#     print("오류 발생! ")

# 숫자를 입력하지 않은 경우
# try:
#     num = int(input("숫자를 입력하세요 : "))
# except ValueError:
#     print("숫자가 아닙니다.")


# 에러종류 명시 : as 에러 메시지 변수
# try:
#     num = int(input("숫자를 입력하세요 : "))
# except ValueError as e:
#     print("숫자가 아닙니다.",e)

a = [1,2,3]
# try:
#     print(a[4])
#     print(10/0)
# except ZeroDivisionError as e:
#     print("0으로 나눌 수 없습니다.")
# except IndexError as e:
#     print(e)

try:
    print(a[4])
    print(10/0)
except (ZeroDivisionError,IndexError) as e:
    print("오류 발생 ",e)


# else 문 수행 - 예외가 발생하지 않는 경우
