
# 입력받은 문자열을 공백기준으로 나눈뒤에
# map함수를 이용하여 각각 정수형으로 (int)바꾼뒤에 n,k에 넣는다
# split() 입력값을 두 개 이상으로 분리

n, k = map(int, input().split())

# result는 우리가 총 연산을 실행하는 횟수
result = 0

while True:

    target = (n // k) * k

    # 1을 빼는 몇번 실행 할 지 알려주는 코드
    result = result + (n - target)

    # 빼고 난 뒤에 n이 target이라고 설정!
    n = target

    if n < k:
        break

    # k로 나누는 연산을 한번 수행하기 때문에
    result = result + 1
    n = n // k

# 마지막으로 남은 수에 대하여 1씩 빼기
result = result + (n - 1)
print(result)

