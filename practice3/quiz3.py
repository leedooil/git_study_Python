from itertools import count


# pwd = "http://naver.com"
# pwd1 = pwd[7:]
# # print(pwd1)
# pwd2 = pwd1[:5]
# # print(pwd2)
# pwd3 = len(pwd2)
# # print(pwd3)
# pwd4 = pwd2[:3]
# pwd5 = pwd2.count("e")

# print(pwd4 + str(pwd3) + str(pwd5) + "!")


# 해설

url = "http://naver.com"
my_str = url.replace("http://","")
# print(my_str)
my_str = my_str[:my_str.index(".")]
# print(my_str)
pwd = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0}의 비밀번호는 {1}입니다.".format(url, pwd))
