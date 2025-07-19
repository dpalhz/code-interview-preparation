def solution(A):
    total = sum(A)
    left_sum = 0
    min_diff = float('inf')

    for i in range(1, len(A)):
        left_sum += A[i - 1]
        right_sum = total - left_sum
        diff = abs(left_sum - right_sum)
        min_diff = min(min_diff, diff)
        
    return min_diff