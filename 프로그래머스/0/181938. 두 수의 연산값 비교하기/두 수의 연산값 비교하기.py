def solution(a, b):
    answer = 0
    
    a_b = int(f"{a}{b}")

    product = 2 * a * b
    
    if a_b >= product:
        return a_b
    else:
        return product
    
    return answer