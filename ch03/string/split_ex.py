# split_ex

birthday = input("생일 입력 (연/월/일) : ")

birth_list =birthday.split('/')

# print(birth_list) ['1997','10',15]

print("당신은 %s 에 태어났고 생일은 %s 월 %s일이군요"%(birth_list[0],birth_list[1],birth_list[2]))

