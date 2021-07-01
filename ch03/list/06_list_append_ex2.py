st_list = []
total = 0
count =0
st_num = int(input("학생 수 입력 : "))

for i in range(0,st_num):
    score = int(input("학생%d 점수 입력 : " %(i+1)))
    st_list.append(score)
    total += st_list[i]
    if st_list[i] >= 80 :
        count += 1


print("총점 : %d" %total)
print("평균 : %.2f" %(total/len(st_list)))

print("80점 이상 학생 : %d 명" %count)