def solution(X, Y, D):
    gap = Y - X
    result = gap // D
    remains = gap % D
    if remains != 0:
        return result + 1
    else:
        return result