def solution(str1, str2):
    answer = ""
    for i in range(min(len(str1), len(str2))): 
        answer += str1[i] + str2[i]
    
    answer += str1[i+1:] + str2[i+1:] 
    return answer
