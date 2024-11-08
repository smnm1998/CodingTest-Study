def solution(my_string, m, c):
    answer = ''
    
    for i in range(0, len(my_string), m):
        row = my_string[i:i+m]
        
        if len(row) >= c:
            answer += row[c-1]
            
    print(answer)
    return answer