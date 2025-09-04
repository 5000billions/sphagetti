T = int(input())  
for tc in range(1, T + 1):  
    N = int(input())  
    C = list(map(int, input()))  

    # 연속된 1의 개수 카운트
    one = 0   
    # 지금까지 나온 최대 연속 1의 개수
    best = 0  

    # 배열을 하나씩 순회
    for i in C:  
        # 현재 값이 1이면
        if i == 1:  
            # 연속된 1 개수 증가
            one += 1  
            # 지금까지의 최대값보다 크다면 갱신
            if one > best:  
                best = one  
        else:  
            one = 0  # 0을 만나면 다시 0으로 초기화
    
    print(f"#{tc} {best}")
