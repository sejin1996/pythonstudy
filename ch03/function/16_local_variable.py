# 16_local_variable.py

#예제 함수 정의

def show():
    a=1             # 함수 내에서 정의된 지역변수
    a=a+1
    print(a)        # 변수 a 는 함수 내에서만 사용가능 / 화면에 변수 값 2를 출력

show()  # 함수 호출하면 함수로 이동 후 함수문장실행. 실행 종료 후 다시 호출한 곳으로 복귀한다.

# show(a)       Error 발생 . 지역 변수이기 때문에 a 가 정의도있지 않다. 
