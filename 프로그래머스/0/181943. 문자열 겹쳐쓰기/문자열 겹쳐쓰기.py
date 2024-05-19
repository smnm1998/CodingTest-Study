def solution(my_string, overwrite_string, s):
    answer = my_string[:s] + overwrite_string + my_string[s+len(overwrite_string):]
    return answer

# + my_string[s+len(overwrite_string):]를 붙여야 뒤에 남아있는 문자열이 출력된다.
# 테스트 2 처럼 끝까지 출력하는 것이라면 상관없지만, 테스트 1에서는 뒤의 d를 출력하기 위해서는 뒤에 붙여줘야 한다.