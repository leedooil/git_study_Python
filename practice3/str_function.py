python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python","Java"))

index = python.index("n")
print(index)

index = python.index("n", index+1)
print(index)

print(python.find("n"))

print(python.find("Java")) # 문자열이 없어도 오류 안내고 대신 -1로 반환함

print(python.index("Java")) # 문자열이 없으면 바로 오류냄