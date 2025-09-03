T = int(input())

for tc in range(1, T+1):  #테스트 케이스 
    N, M = map(int, input().split()) # N개의 숫자로 구성된 숫자열
                                    #M개의 숫자로 구성된 숫자열

    ai = list(map(int, input().split())) #N의 숫자열 입력
    bi = list(map(int, input().split())) #M의 숫자열 입력 

     
    if N >= M:             #만약 N이 M보다 크거나 같으면
        long_arr, short_arr = ai, bi  # 긴배열이 ai 짧은 배열이 bi
        L, S = N, M                   
    else:#만약 M이 N보다 크면 
        long_arr, short_arr = bi, ai # 긴배열이 bi 짧은 배열이 ai
        L, S = M, N

    max_v = -10**10  #음수도 나올 수 있기에 0을 놔둬선 안된다. 최댓값이 0으로 출력되기에
    for i in range(L-S+1):   # 짧은 배열을 긴배열 위에 포개면 
                                # 짧은 배열이 움직일 수 있는 범위가 나오는데 
                                # N에서 M을 뺀 수가 움직일 수 있는 범위 
        total = 0
        for j in range(S):    # 짧은 배열이 움직일 수 있는 범위
            total += long_arr[i+j] * short_arr[j]

        if total > max_v:    #최대값을 비교
            max_v = total   #만약 total이 최댓값보다 크면   
                            # max_v = total이된다. 


    print(f'#{tc} {max_v}')