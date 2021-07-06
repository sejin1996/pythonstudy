# 04_class4메서드

# 클래스 정의
# name, age 2개의 속성읠 정의 - 생성자 파라미터로 기본값을 저장
class person:
    # 생성자 함수
    def __init__(self,name,age=10):
        self.name = name
        self.age = age
        print(self,'is generated')
    # 클래스 매서드 (sleep()  -xxx는 잠을 잡니다 출력)

    def sleep(self):
        print('self : ',self)
        print(self.name, '은 잠을 잡니다.')

class Rectangle :
    # 생성자 함수
    def __init__(self,width,height):
        self.width = width
        self.height = height
    # 클래스 매서드 (calcArea()-넓이를 계산해 반환)
    def calcArea(self):
        area = self.width*self.height
        return area


## 객체 인스턴스 생성 및 사용
a = person('Aaron',20)
b = person('bob',30)

a.sleep()
b.sleep()

r_1 = Rectangle(10,30)
r_2 = Rectangle(3.5,2.1)

print("면적 r_1 :",r_1.calcArea())
print("면적 r_2 :",r_2.calcArea())
