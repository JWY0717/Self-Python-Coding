def solution(x, n):
    answer = []
    result = 0
    for i in range(1, n + 1):
        answer.append(x * i)

    return answer

# 요소를 추가할 수 있는 함수
# append
# >>> nums = [1, 2, 3]
# >>> nums.append(4)
# [1, 2, 3, 4]

# >>> nums.append([5, 6])
# [1, 2, 3, 4, [5, 6]] # 리스트가 하나의 객체로 추가되었음