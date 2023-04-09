# 기준 데이터를 설정하고, 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법

# 왼쪽은 5보다 큰 것을 고르고
# 오르쪽은 5보다 작은 것을 골라서
# 서로의 위치를 바꾼다

#결과
# 왼쪽에 있는 데이터는 모두 5보다 작고
# 오른쪽에 있는 데이터는 모두 5보다 크다

array = [5,7,9,0,3,1,6,2,4,8]
def quick_sort(array):
    #리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array
    pivot = array[0] # 피벗은 첫 번째 원소
    tail = array[1:] # 피벗을 제외한 리스트

    # pivot을 제외한 리스트에
    # pivot 값 보다 작은 경우에는 왼쪽 리스트에 담게 한다
    left_side = [x for x in tail if x <= pivot] #분할이 된 왼쪽 부분

    # pivot 값 보다 큰 경우에는 오른쪽 리스트에 담게 한다
    right_side = [x for x in tail if x > pivot] #분할된 오른쪽 부분

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)
print(quick_sort(array))

