def solution(A, K):
    if not A:  # Cek jika A kosong
        return []

    rotate = K % len(A)
    return A[-rotate:] + A[:-rotate]