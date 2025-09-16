T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    max_len = 0

    # 행 기준으로 최장 길이 찾기
    for i in range(N):
        length = 0
        for j in range(M):
            if grid[i][j] == 1:
                length += 1
                if length >= 2 and length > max_len:
                    max_len = length

            else:
                length = 0

    # 열 기준으로 최장 길이 찾기
    for j in range(M):
        length = 0
        for i in range(N):
            if grid[i][j] == 1:
                length += 1
                if length >= 2 and length > max_len:
                    max_len = length

            else:
                length = 0      

    print(f"#{tc} {max_len}")