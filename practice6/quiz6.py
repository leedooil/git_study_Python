# def std_weight(height,gender):
#     if gender == "남자":
#         print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다."\
#             .format(height*100,gender,round((height*height*22),2)))
#     else:    
#         print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다."\
#             .format(height*100,gender,round((height*height*21),2)))

# std_weight(1.75,"남자")    
# std_weight(1.60,"여자")

# 정답
    
def std_weight(height,gender): # 키 m 단위 (실수), 성별 "남자" / "여자"
    if gender == "남자":
        return height * height * 22
    else:    
        return height * height * 21

height = 175 # cm 단위
gender = "남자"
weight = round(std_weight(height / 100, gender),2)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height,gender,weight))