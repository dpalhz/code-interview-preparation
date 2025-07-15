def solution(A, K):
    if not A:  
        return []
    rotate = K % len(A)
    return A[-rotate:] + A[:-rotate]