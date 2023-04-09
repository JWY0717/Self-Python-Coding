array = [7,5,9,0,3,1,6,2,4,8]

for i in range (len(array)):
    Min_index = i #제일 작은 원소의 인덱스
    for j in range(i +1, len(array)):
        if array[Min_index] > array[j]:
            Min_index = j
    array[i], array[Min_index] = array[Min_index], array[i] # 두 원소의 위치를 빠구는 스와프 사용
print(array)
