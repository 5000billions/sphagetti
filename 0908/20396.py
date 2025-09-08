T = int(input())
for tc in range(1, T + 1):

    # N, M = N개의 돌, M은 i,j가 몇줄인지
    N, M = map(int, input().split())
    # 작은 돌 배열
    arr = list(map(int, input().split()))
    for _ in range(M):
        i, j = map(int, input().split())

        # i와 j는 인덱스랑 다르게 1부터 시작하여서
        # -1을 해주고 시작
        # 배열 밖으로 안나가게 N밑으로 조건문
        # k
        for k in range(i-1, i+j-1):
            if k < N:
                # i 번째 돌로 깔맞춤
                arr[k] = arr[i-1]

    # 리스트를 공백으로 구분해 문자열로 변환
    rock_arr = ''.join(map(str, arr))

    print(f"#{tc} {rock_arr}")