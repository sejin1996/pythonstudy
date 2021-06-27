

notebook = 1200000
digitalCam = 400000


print("*********상품 정보 ************")
print("1 노트북 : %s 원"%format(notebook, ","))
print("2 디지털카메라 : %s 원"%format(digitalCam,","))
print("*******************************")

serialN = int(input("상품 번호입력 : "))
if serialN == 1 or serialN == 2:
    num = int(input("주문 수량 입력 : "))
    if serialN ==1 :
        product = '노트북'
        S_price = notebook
        price = notebook * num
        if price >= 1000000 :
            dc = 0.1 * price
        elif price >= 500000 :
            dc = 0.05 * price
        else:
            dc = 0
    else:
        price = digitalCam * num
        product = '디지털 카메라'
        S_price = digitalCam
        if price >= 1000000 :
            dc = 0.1 * price
        elif price >= 500000 :
            dc = 0.05 * price
        else:
            dc = 0
    ##

    print("***********주문 내용***********")
    print("상품명 : %s" % product)
    print("가격 : %s 원" % format(S_price,','))
    print("주문 수량 : %d" % num)
    print("주문액 : %s원" % format(price,','))
    print("할인액 : %s원" % format(int(dc),","))
    print("총 지불액 : %s원" %format(int(price - dc),','))



else:
    print("잘못 입력하였습니다. 종료합니다.")
