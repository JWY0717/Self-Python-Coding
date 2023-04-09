String = input()

# 첫 번째 문자를 숫자로 변경하여 대입한다
result = int(String[0])

for i in range(1,len(String) ):

    num = int(String[i])
    if num <=1 or result <= 1:
        result = result + num
    else:
        result = result * num
print(result)
