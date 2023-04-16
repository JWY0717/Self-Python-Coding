# step 1
# 첫번째 시작점:0  끝점: 19로 설정 중간점:9
# 이때 필요한 떡의 크기 : M = 6이므로 결과를 저장

# step2
# 시작점을 10, 끝점:19 중간점: 14
# 이때 필요한 떡의 크기 : M = 6이므로 결과 저장


# step3
# 시작점을 중간점보다 1큰 값으로 설정
# 시작점을 15, 끝점:19 중간점: 17
# 이때 필요한 떡의 크기 : M = 6이므로 결과 저장

#===== 중간점의 값은 "시간이 지날 수록 "최적화된 값"이 되기 때문에.
# 과정을 반복하면서 얻을 수 있는 떡의 길이합이 필요한 떡의 길이보다
# 크거나 같을 때마다 "중간점의 값을 기록"하면 됩니다..!!!

# 떡의 개수 N, 요청한 떡의 길이 M

n, m = map(int, input().split())

# 떡의 개별 높이a
array = list(map(int, input().split()))

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array)

# 이진 탐색 수행 (반복적)
result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        # 잘랐을 때의 떡의 양을 계산
        if x > mid:
            total = total + (x - mid)
        # 떡의 양이 부족한 경우 더 많이 자르기 (왼쪽 부분 탐색)
    if total < m:
        end = mid - 1

        # 떡의 양이 부족한 경우 덜 자르기  (오른쪽 부분 탐색_
    else:
        result = mid # 최대한 덜 잘랐을 때가 정답이므로,,, 여기에서 return에 기록
        start = mid + 1
#정답을 출력
print(result)


