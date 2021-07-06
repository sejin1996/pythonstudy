# 06_file_readlines.py

# readlines() 함수를 이용해서 전체 라인 읽어오기

print('--------전체라인 읽고 출력---------')

f1 = open("test.txt",'r')
lines = f1.readlines()
print(lines)
f1.close()

f2 = open("test.txt",'r')
lines = f2.readlines()
for line in lines:
    print(line,end='')
f2.close()
##------------------------------#####
f3=open('test.txt','r')         # f3 파일객체 - 반복문에 바로 반복요소로 사용가능

for line in f3:
    print(line,end='')

f3.close()

