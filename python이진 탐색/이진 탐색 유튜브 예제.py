
# 인덱스 0이 첫번째 지점
# 인덱스 9가 마지막 지점
# 중간점은 4


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
    #찾은 경우 중간점 인덱스 변환
        if array[mid] == target:
            return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽을 확인한다
        elif array[mid] > target:
            end = mid - 1
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽을 확인
        else:
            start = mid + 1
    result  None
# n(원소의 개수)과 target(찾고자 하는 값)을 입력 받기
n, target = list(map(int, input().split()))

# 전체 원소 입력 받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)