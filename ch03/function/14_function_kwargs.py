# 14_function_kwargs.py

# 가변길이 매개변수 : **kwargs
# keyword arguments 의 약자, key=value 형태로 값을 받는다.

def show_keywords(**kwargs):
    print(kwargs)
    print(type(kwargs))

show_keywords() #빈 dict 가 전달된다. 

show_keywords(id='sun,',
              name ='kim',
              phone='010-1234-1234'
              )
show_keywords(
    num=3,
    val='kim',
    str='abcdef'
)
