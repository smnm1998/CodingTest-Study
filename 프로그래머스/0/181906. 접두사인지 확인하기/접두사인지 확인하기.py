def solution(my_string, is_prefix):
    answer = 0
    string =""
    for i in range(len(my_string)):
        string = my_string[:i+1]
        if string == is_prefix:
            return 1
    return 0