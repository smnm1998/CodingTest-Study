def solution(num_list):
    product = 1
    sum_elements = 0
    
    for num in num_list:
        product *= num
        sum_elements += num
        
    sum_squared = sum_elements ** 2
    
    if product < sum_squared:
        return 1
    else:
        return 0