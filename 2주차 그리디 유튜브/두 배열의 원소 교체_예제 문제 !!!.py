n , k = map(int, input().split())

# 배열 A는 오름차순으로 정렬
A = list(map(int,input().split()))

list_A = sorted(A)

# 배열 B는 내림차순으로 정렬

B = list(map(int,input().split()))

list_B = sorted(B, reverse=True)

# 두 배열의 원소를 첫 번째 인덱스 부터 차례로 확인 하면서
#배열 A와 B의 원소를 k번쨰 수들 만큼 서로 바꾸면 완성

for i in range (len(list_B)):
    if list_A[i]  <  list_B[i]:
        #list_A의 원소를 바꾸는 법!!!!!!1
        list_A[i],list_B[i] = list_B[i],list_A[i]
    else:
        break

print(sum(list_A))




