# gun = 10 # 전역변수 : 전체에서 사용가능

# def checkpoint(soldiers):
#     gun=20 # 지역변수 : 함수 내에서만 사용가능
#     gun=gun-soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))

# print("전체 총 : {0}".format(gun))
# checkpoint(2) # 2명이 경계 근무 나감    
# print("남은 총 : {0}".format(gun))    


# gun = 10 # 전역변수 : 전체에서 사용가능

# def checkpoint(soldiers):
#     global gun # 전역 공간에 있는 변수 사용가능
#     gun=gun-soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))

# print("전체 총 : {0}".format(gun))
# checkpoint(2) # 2명이 경계 근무 나감    
# print("남은 총 : {0}".format(gun))    

gun = 10 # 전역변수 : 전체에서 사용가능

def checkpoint(soldiers):
    global gun # 전역 공간에 있는 변수 사용가능
    gun=gun-soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun=gun-soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
# checkpoint(2) # 2명이 경계 근무 나감
gun=checkpoint_ret(gun,2)    
print("남은 총 : {0}".format(gun))    