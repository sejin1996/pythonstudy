#학생 5명의 점수를 입력받아 리스트에 추가

# 3명의 회원을 입력받아리스트에 추가, 리스트 내용 출력

st_list = []
total = 0

for i in range(0,5):
    score = int(input("학생%d 점수 입력 : " %(i+1)))
    st_list.append(score)
    total += st_list[i]

print("총점 : %d" %total)
print("평균 : %.2f" %(total/len(st_list)))






