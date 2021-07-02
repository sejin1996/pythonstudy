# 15_function_args

#키워드 인수 예제

# 학생 정보를 입력받아 학생 dict 를 구성하여 반환하는 함수

def student_info(name,age,gender):
    student={
        'name':name,
        'age':age,
        'gender':gender
    }
    return student

# 함수 테스트
# 함수 호출시 인수를 넘겨 dict 가 제댈 ㅗ구성되어 반환되는지 출력

print(student_info(name="kim",gender="여",age=23))   #키워드 인수
print(student_info('lee',20,'남'))
print(student_info('park',gender='남',age=25))
