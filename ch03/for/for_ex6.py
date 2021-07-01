for i in range(1,6): #1~5
    for j in range(0,6-i):
        print("*",end='')
    print()

for i in range(0,5): #0~4
    for j in range(4,i,-1):
        print(" ",end='')
        #별 찍기
    for k in range(0,i*2+1):
        print('*',end='')
    print()
    