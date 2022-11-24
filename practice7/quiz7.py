# index = 1
# with open(str(index)+"주차.txt", "w", encoding="utf8") as report_file:
#     while index <= 50:
#         report_file.write(""" - {0} 주차 주간보고 -
#                               부서 :
#                               이름 :
#                               업무 요약 :""".format(index))
#         index+=1

# index = 1
# while index <= 5:
#     with open(str(index)+"주차.txt", "w", encoding="utf8") as report_file:
#         report_file.write("""- {0} 주차 주간보고 -
# 부서 :
# 이름 :
# 업무 요약 :
# """.format(index))
#         index+=1

# 정답
for i in range(1,51):
    with open(str(i)+"주차.txt", "w", encoding="utf8") as report_file:
        report_file.write("- {0} 주차 주간보고 -".format(i))
        report_file.write("\n부서 :")
        report_file.write("\n이름 :")
        report_file.write("\n업무요약 :")