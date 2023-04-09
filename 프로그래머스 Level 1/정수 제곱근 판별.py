def solution(n):
    Wow = n ** (1/2)
    if Wow % 1 ==0:
        return (Wow + 1 ) ** 2
    else:
        return -1