def solution(ineq, eq, n, m):
    if ineq == '>' and eq == '=':
        return 1 if n >= m else 0
    elif ineq == '<' and eq == '=':
        return 1 if n <= m else 0
    elif ineq == '>' and eq == '!':
        return 1 if n > m else 0
    elif ineq == '<' and eq == '!':
        return 1 if n < m else 0
    else:
        return 0  # 이 경우는 실제로 발생하지 않겠지만, 예외 처리를 위해 추가