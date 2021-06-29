# w중첩 구구단
# 구구단 출력 2단부터 9단까지 출력


# for dan in range(2,10):
#     for n in range(1,10):
#         print("%d * %d = %d"%(dan,n,dan*n))
#     print()


# 한줄에 구구단 전부 표시
# for n in range(1,10):
#     for dan in range(2,10):
#         print("%d * %d = %d"%(dan,n,dan*n), end="\t")
#     print()


# 한줄에 구구단 전부 표시 + 숫자 위치 통일하려면 %2s
for n in range(1,10):
    for dan in range(2,10):
        print("%d * %d = %2s"%(dan,n,str(dan*n)), end="\t")
    print()

