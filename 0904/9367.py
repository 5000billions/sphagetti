T = int(input())  
for tc in range(1, T + 1):  

    N = int(input())  
    C = list(map(int, input().split()))  

    # 연속 증가 길이 초기값 1
    carrot = 1  
    # 지금까지 최댓값 초기값 1
    best = 1    

    # 당근 배열 연속 증가 확인
    for i in range(N - 1):  
        # 다음 당근이 더 크면
        if C[i + 1] > C[i]:   
            # 연속 증가 길이 +1
            carrot += 1       
        # 연속이 끊겼다면 지금까지 연속 길이가 최대라면 갱신   
        else:                 
            if carrot > best:  
                best = carrot
            # 연속 길이 다시 1로 초기화    
            carrot = 1        

    # 반복이 끝난 뒤 마지막 구간도 체크
    if carrot > best:
        best = carrot

    print(f"#{tc} {best}")
