#학생 5명의 점수를 입력받아 리스트에 추가
# 80점 이상 학생의 수를 계산하여 출력

st_list = []
total = 0
count =0

for i in range(0,5):
    score = int(input("학생%d 점수 입력 : " %(i+1)))
    st_list.append(score)
    total += st_list[i]
    if st_list[i] >= 80 :
        count += 1


print("총점 : %d" %total)
print("평균 : %.2f" %(total/len(st_list)))

print("80점 이상 학생 : %d 명" %count)

# 내림 차순 정렬
st_list.sort(reverse=True)      #내림차순 정렬
print(st_list)

a= 484
b=207
print(a+b)