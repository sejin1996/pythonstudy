# 01_module1.py

# 실행 코드
# 생성한 모듈 new_calculator import

import new_calculator

from new_calculator import sub      #sub 함수 import
from new_calculator import *    # 모듈안에 있는 모든 함수 import
a=new_calculator.add(7,4)

print(a)

# sub 함수를 import 했으므로 앞에 모듈명을 적지 않과 함수 명만 적어 사용 가능
s = sub(7,4)
print(s)

m=mul(7,4)
print(m)

d=div(7,4)
print(d)

