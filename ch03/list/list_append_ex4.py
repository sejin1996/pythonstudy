#상품을 리스트에 추가
# 엔터키를 누르면 입력 종료되고 등록된 상품 리스트 출력

product_list = []
while True:
    product = input("상품 등록 (엔터키 누르면 종료): ")
    product_list.append(product)
    if product == "":
        break
print(product_list[0:len(product)-1])

