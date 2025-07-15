def solution(N):
    start = False
    result = 0 
    count = 0
    while N > 0:
        i = N % 2
        if i == 1:
            if result < count:
                result = count
            start = True
            count = 0
        if i == 0 and start:
            count += 1
        N = N // 2
    return result


