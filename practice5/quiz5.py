# from random import random

# # index = 1
# # print(passenger)

# total = 0
# for index in range(1,51):
#     passenger = int(random()*50+1)
#     if 5<=passenger<=15:
#         print("[O] {0}번째 손님 (소요시간 : {1})".format(index, passenger))
#         total+=1
#     else:
#         print("[X] {0}번째 손님 (소요시간 : {1})".format(index, passenger))
# print("총 탑승 승객 : {0} 분".format(total))        
        
# # while index <= 50:
# #       if 5 <= passenger <= 15:
# #           print("[O] {0}번째 손님 (소요시간 : {1})".format(index, passenger))
# #       index += 1

# 정답
from random import *

cnt = 0 # 총 탑승 승객 수
for i in range(1,51): # 1 ~ 50 이라는 수 (승객)
    time = randrange(5, 51) # 5분 ~ 50분 소요 시간 
    if 5<= time <=15: # 5분 ~ 15분 이내의 손님(매칭 성공), 탑승 승객 수 증가
        print("[O] {0}번째 손님 (소요시간 : {1})".format(i, time))
        cnt+=1
    else: # 매칭 실패한 경우
        print("[ ] {0}번째 손님 (소요시간 : {1})".format(i, time))
print("총 탑승 승객 : {0} 분".format(cnt))        
      
          
      
      
        
    
    
    
    
    
    
    
    