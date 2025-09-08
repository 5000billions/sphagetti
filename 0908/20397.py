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
        c = i - 1                      # 중심 고정

        for k in range(1, j + 1):      # 좌우로 k칸씩 퍼지며 확인
            L = c - k
            R = c + k

            # 범위 체크 인덱스 밖이면 의미 없으므로 break
            if L < 0 or R >= N:
                break

            # 좌우 값이 같으면 둘 다 변경
            if arr[L] == arr[R]:
                # 왼쪽 
                if arr[L] == 0:
                    arr[L] = 1
                else:
                    arr[L] = 0

                # 오른쪽 
                if arr[R] == 0:
                    arr[R] = 1
                else:
                    arr[R] = 0

    print(f"#{tc} {' '.join(map(str, arr))}")