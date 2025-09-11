"""
처음 변경전
00 10 20 
01 11 21
02 12 22

90' 시계 
02 01 00
12 11 10
22 21 20

180' 시계
22 12 02
21 11 01
20 10 00

270' 시계
20 21 22
10 11 12
00 01 02
"""
    
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]
    
    # 90도
    degree90 = [[arr[N-1-j][i] for j in range(N)] for i in range(N)]
    # 180도
    degree180 = [[arr[N-1-i][N-1-j] for j in range(N)] for i in range(N)]
    # 270도
    degree270 = [[arr[j][N-1-i] for j in range(N)] for i in range(N)]

    print(f"#{tc}")
    for i in range(N):
        print("".join(degree90[i]), "".join(degree180[i]), "".join(degree270[i]))
