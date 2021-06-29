# slicing

crawling ="Data crawling is fun"

print(crawling)

print(crawling[0])  #첫번쨰 문자
print(crawling[-1]) #마지막 문자
print(crawling[2])  #인덱스 2번, 3번째 문자

#슬라이싱 예제
print(crawling[0:4])        #0~3번 인덱스 까지
print(crawling[5:16])       #5~15 인덱스 까지
print(crawling[17:])        #17~끝까지
print(crawling[19])         #인덱스 19번 문자
print(crawling[-1:])         #시작은 마지막 문자에서 끝까지 - 마지막 문자
print(crawling[-1])         #위코드와 동일

print(crawling[:-1])            #처음부터 마지막 문자 전까지
print(crawling[16:16+4])
