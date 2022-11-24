# print("Python","Java")
# print("Python"+"Java")
# print("Python","Java",sep=",")
# print("Python","Java",sep=" vs ")
# print("Python","Java","JavaScript",sep=" vs ")

# print("Python","Java",sep=",")
# print("무엇이 더 재밌을까요?")

# print("Python","Java",sep=",",end="?")
# print("무엇이 더 재밌을까요?")

# import sys
# print("Python", "Java", file=sys.stdout) # 표준 출력
# print("Python", "Java", file=sys.stderr) # 표준 에러

# # 시험 성적
# scores = {"수학":0,"영어":50,"코딩":100}
# for subject, score in scores.items():
#     # print(subject,score)
#     print(subject.ljust(4),str(score).rjust(4),sep=":")

# # 은행 대기순번표
# # 001, 002, 003, ...
# for num in range(1,21):
#     print("대기번호 : "+str(num).zfill(3))

#input으로 값을 넣으면 무조건 str형임
answer = input("아무 값이나 입력하세요 : ")
print(type(answer))
print("입력하신 값은 "+answer+"입니다.")