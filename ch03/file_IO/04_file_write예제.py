# 04_file_write예제
# 사용자로부터 회원이름을 입력받아 파일에 저장하시오

f = open("file_member.txt",'w',encoding='utf-8')

for i in range(1,6):
    member = input("회원이름을 입력하세요 : ")
    data = member+'\n'
    f.write(data)
f.close()
