def solution(a, b):
    # 두 정수를 문자열로 이어 붙인 값 생성
    a_b = int(f"{a}{b}")
    b_a = int(f"{b}{a}")
    
    # 두 값 중 더 큰 값을 반환
    if a_b >= b_a:
        return a_b
    else:
        return b_a