
def solution(n):
    #우선 n의 값이 정수로 주어지기 때문에 문자값으로 바꿔서 n_1 담는다!
    n_1 = list(str(n))
    # t에서 sort를 통해 내림차순 정렬을 해준다.
    n_1.sort(reverse=True)
    # 서 str값으로 바꾸어 담은 값이기 때문에 int로 형변환
    answer = int("".join(n_1))
    return answer