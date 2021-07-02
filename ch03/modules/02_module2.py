# 02_module2

# import 시 동일 디렉토리가 아닌경우
# from 디렉토리명 import 모듈명
from module import a        # a 모듈명만 import - a.함수명() 형식으로 사용가능
from module import b        # b 모듈명만 import - b.함수명()   형식으로 사용가능
from module.b import *      # 모든 함수 까지 import - 함수명()  형식으로 사용가능

import module.a     # import 시 모듈을 찾지 못한다.
import module.b     # import 시 모듈을 찾지 못한다.

a.hello("홍길동")
hello_1()

