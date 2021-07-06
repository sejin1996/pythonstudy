# 02_file_write1

#data='hi'
data='안녕하세요'
# f=open("file2.txt",'w')
# f.write(data)
# f.close()

f=open("file3.txt",'w',encoding='utf-8')
f.write(data)
f.close()