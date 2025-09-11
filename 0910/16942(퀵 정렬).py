# arr은 정렬 대상 배열
# l, r 정렬 범위의 시작 인덱스, 종료 인덱스(둘 다 포함)
def quicksort(arr, l, r):
    # l < r 인 동안에만 정렬 (원소가 0개/1개면 종료)
    if l < r:
        # 기준원소(피벗)를 확정하고 그 위치 p를 받는다
        p = partition(arr, l, r)

        # 기준원소의 왼쪽 구간 [l, p-1] 정렬
        quicksort(arr, l, p - 1)
        # 기준원소의 오른쪽 구간 [p+1, r] 정렬
        quicksort(arr, p + 1, r)


def partition(arr, l, r):
    # 기준원소(피벗)는 현재 구간의 가장 왼쪽 원소로 선택
    p = arr[l]

    # p보다 작은 원소는 왼쪽으로, 큰 원소는 오른쪽으로 보낼 것
    # i : 왼쪽에서 오른쪽으로 진행하며 p보다 큰 첫 원소를 찾는 인덱스
    i = l
    # j : 오른쪽에서 왼쪽으로 진행하며 p보다 작은 첫 원소를 찾는 인덱스
    j = r

    # i와 j가 교차하기 전까지 반복
    while i <= j:
        # 왼쪽에서부터 p보다 큰 원소를 찾을 때까지 i 전진
        while i <= j and arr[i] <= p:
            i += 1

        # 오른쪽에서부터 p보다 작은 원소를 찾을 때까지 j 후진
        while i <= j and arr[j] >= p:
            j -= 1

        # 아직 i < j 이면 양쪽에서 자리 틀린 원소를 찾은 상태 -> 서로 교환
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    # 여기 도달하면 i와 j가 교차한 상태
    # 기준원소 p를 j 위치(작은 쪽 구간의 맨 끝)와 교환하여 위치를 확정
    arr[l], arr[j] = arr[j], arr[l]

    # 기준원소의 최종 위치 j를 반환
    return j


T = int(input().strip())
for tc in range(1, T + 1):
    N = int(input().strip())                 # 정수의 개수
    arr = list(map(int, input().split()))    # 정렬할 배열

    # 전체 구간 퀵정렬 수행
    quicksort(arr, 0, N - 1)

    # 중앙값 출력 (N//2 번째 원소)
    print(f"#{tc} {arr[N // 2]}")