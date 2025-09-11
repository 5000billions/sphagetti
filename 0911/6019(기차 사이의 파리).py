T = int(input())
for tc in range(1, T + 1):
    D, A, B, F = map(int, input().split())
    # N = 시간
    N = D / (A + B)
    dis = N * F
    
    print(f"#{tc} {dis}") 