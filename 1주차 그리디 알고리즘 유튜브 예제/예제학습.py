a= 1000
print(a)

b= 157.13
print(b)

c= int(78478)
print(c)

d= 1230.456
print(d)

#반올림 목적으로 사용
d1 = round(1230.456,2)
print(d1)

q= 2
w= 4

#거듭 제곱
print(q ** w)

#제곱근
print(q ** 2)


# 리스트 컴프리헨션의 예시
# 여러 줄의 코딩 방식을 한 줄로 줄일 수 있다
array = [ i  for i in range(10)]
print(array)

array = [ i  for i in range(10) if i % 2 == 1]
print(array)


array = [ i * i for i in range (1,10)]
print(array)


answer = 0
for i in range (1,10):
    answer = answer + i
print(answer)


a= [1,2,3]
a.append(4)
print(a)

a.sort()
print(a)

a.sort(reverse=True)
print(a)

a.reverse
print(a)

a.insert(2,8)
print(a)

a.remove(1)
print(a)

a= "ABCDE"
print(a[0:2])

a=dict()
a['장우영'] =  27
a['장유정'] =  24
print(a)

b = { '장우영' : 27,
      '장유정' : 24
    }
print(b)
print("++++++++++++++++++++++++++++++++++++++++++")
key_list = b.keys()
key_list = list(b.keys())
print(key_list)

values_list = a.values()
values_list = list(a.values())
print(values_list)
print(a['장우영'])

print("++++++++++++++++++++++++++++++++++++++++++")