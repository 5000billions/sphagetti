T = int(input())  
for tc in range(1, T + 1):  
    N = int(input())  
    A = list(map(int, input().split()))  

    # 증가하는 곱의 최댓값. 없으면 -1 유지
    ans = -1  

    # 모든 서로 다른 두 수 쌍 (i < j)이 맞는지 확인
    for i in range(N - 1):               
        for j in range(i + 1, N):        
            # 두 수의 곱
            p = A[i] * A[j]              

            # 곱 p가 단조 증가인지 확인
            # 자리수 비교를 위해 문자열로 바꿈
            s = str(p)                 
            # 1이면 단조 증가 통과, 0이면 실패  
            ok = 1                       
            # 인접 자리끼리 비교하기
            for k in range(len(s) - 1):  
                # 앞자리 > 뒷자리면 단조 증가 X
                if s[k] > s[k + 1]:  
                    # 실패시 즉시 종료
                    ok = 0               
                    break                

            # 단조 증가면 최댓값 갱신
            if ok:
                if p > ans:
                    ans = p

    print(f"#{tc} {ans}")
