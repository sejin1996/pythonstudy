# 3명의 회원을 입력받아리스트에 추가, 리스트 내용 출력

commu = []


for i in range(0,3):
    name = input("회원 입력 : ")
    commu.append(name)

print("회원 명단 : ",commu)


print("==============해설 =====================")

members = []    # 빈 리스트 생성
for i in range(5):
    member = input("회원 입력 : ")
    members.append(member)

# 리스트 내용 출력
print("회원 명단 : ",end='')
for mamber in members:
    print(mamber,end=' ')