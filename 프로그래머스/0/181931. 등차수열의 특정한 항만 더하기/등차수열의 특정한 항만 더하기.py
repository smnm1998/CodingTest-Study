def solution(a, d, included):
    answer = 0
    for i in range(len(included)):
        if included[i]:
            term = a + i * d
            answer += term
    return answer