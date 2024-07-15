def solution(n):
    if n % 2 == 1:  # n이 홀수인 경우
        return sum(i for i in range(1, n + 1, 2))
    else:  # n이 짝수인 경우
        return sum(i * i for i in range(2, n + 1, 2))