def solution(my_string, s, e):
    reverse = my_string[s:e+1][::-1]
    result = my_string[:s] + reverse + my_string[e+1:]
    return result