T = int(input())
for tc in range(1, T + 1):

# K = 최대 이동수
# N = 정류장 종점
# M = 충전소 수
K, N, M = map(int, input().split())
# 충전소 번호
charger_stop = list(map(int,input().split()))

# 정류소 만들기
bus_stop = [0] * (N + 1)
# 충전소 위치 1로 두기
for p in charger_stop:
    bus_stop[p] = 1
# 이동거리(위치), 충전횟수
move = 0
charge = 0
possible = 1

# 도착 전까지 반복
while move + K < N:        
    next_move = move
    # pos에서 K 이내 가장 먼 충전소 찾기 (뒤에서부터 찾기)
    for step in range(K, 0, -1):
        # 
        if bus_stop[move + step]:
            next_move = move + step
            break

    # 충전소가 하나도 없어서 next_pos가 갱신 안 됨 불가능
    if next_move == move:
        possible = 0
        break

    # 이동(충전) 반영
    move = next_move
    charge += 1

# 결과 출력
print(f"#{tc} {charge if possible else 0}")