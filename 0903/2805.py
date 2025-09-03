T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    
    # 농장 들여오기
    grid = [list(map(int, input())) for _ in range(N)]
    # 수확작물 수 초기화
    crop = 0
    
    # 수확 범위 잡기(제일 긴곳을 기준으로 수확할 수 있게 정함)
    d = N // 2

    # 중앙 좌표 정하기
    center = (d, d)

    # for문을 통해 수확 할 수 있는곳을 정하고
    # |이동거리 - 중앙 거리| 해주면 중앙에서 갈 수 있는 거리 나온다
    # 나온 거리를 통해서 grid에 있는 작물들을 더해준다
    for i in range(N):
        for j in range(N):
            if abs(i-d) + abs(j-d) <= d:
                crop += grid[i][j] 

    print(f"#{tc} {crop}")