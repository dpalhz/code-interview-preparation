def solution(A):
    n = len(A)+1
    Sn = int((n/2) * (2 + (n-1)))
    count = 0
    for i in A:
        count += i
    return Sn-count