def solution(code):
    mode = 0  # 초기 mode를 0으로 설정
    ret = []  # 결과를 저장할 리스트 초기화
    
    for idx in range(len(code)):
        if code[idx] == '1':
            mode = 1 - mode  # code[idx]가 '1'이면 mode를 전환
        else:
            if mode == 0 and idx % 2 == 0:
                ret.append(code[idx])  # mode가 0이고 idx가 짝수일 때 ret에 추가
            elif mode == 1 and idx % 2 == 1:
                ret.append(code[idx])  # mode가 1이고 idx가 홀수일 때 ret에 추가
    
    if not ret:
        return "EMPTY"  # ret가 빈 리스트면 "EMPTY" 반환
    
    return ''.join(ret)  # 리스트를 문자열로 변환하여 반환
