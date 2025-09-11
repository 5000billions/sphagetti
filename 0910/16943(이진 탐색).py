# A : 정렬 대상 리스트
# target : 탐색할 값
# return : 조건에 맞게 target을 찾으면 True, 못 찾으면 False
def binary_search(A, target):
    l, r = 0, len(A) - 1         # 탐색 구간의 왼쪽, 오른쪽 인덱스
    last_dir = 0                 # 마지막 탐색 방향 (0: 시작, -1: 왼쪽, 1: 오른쪽)

    # l과 r이 교차하기 전까지 반복
    while l <= r:
        mid = (l + r) // 2       # 중간 위치 계산

        # 중간 값이 target과 같으면 탐색 성공
        if A[mid] == target:
            return True

        # 중간 값이 target보다 크면 왼쪽 구간으로 이동
        elif A[mid] > target:
            # 만약 이전에도 왼쪽으로 갔었다면 규칙 위반 -> 실패
            if last_dir == -1:
                return False
            r = mid - 1          # 오른쪽 끝을 mid-1로 좁힘
            last_dir = -1        # 마지막 방향을 왼쪽으로 기록

        # 중간 값이 target보다 작으면 오른쪽 구간으로 이동
        else:
            # 만약 이전에도 오른쪽으로 갔었다면 규칙 위반 -> 실패
            if last_dir == 1:
                return False
            l = mid + 1          # 왼쪽 끝을 mid+1로 좁힘
            last_dir = 1         # 마지막 방향을 오른쪽으로 기록

    # 끝까지 못 찾으면 False
    return False


T = int(input().strip())           # 테스트 케이스 수
for tc in range(1, T + 1):
    N, M = map(int, input().split())      # A의 원소 수, B의 원소 수
    A = sorted(list(map(int, input().split())))  # A는 반드시 정렬
    B = list(map(int, input().split()))          # 탐색할 B의 원소들

    ans = 0
    # B의 각 원소에 대해 탐색 실행
    for tar in B:
        if binary_search(A, tar):
            ans += 1               # 조건을 만족하며 찾으면 카운트
    
    print(f"#{tc} {ans}")
