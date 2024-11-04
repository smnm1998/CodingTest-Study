def solution(l, r):
    answer = []
    for i in range(l, r+1):
        str_num = str(i)
        if all(c in "05" for c in str_num):
            answer.append(i)
    return answer if answer else [-1]