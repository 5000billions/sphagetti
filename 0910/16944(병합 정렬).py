arr = [] 
# 매개변수는 보기쉽게 시작인 start와 끝인 end로 두기
def merge_sort(start, end): 
    global cnt  # 전역 카운터 사용
    # 재귀함수 종료조건 만들기 병합정렬(분할 정복)을 사용하기 위해
    # 분할을 먼저하는데 분할을 할때 더이상 분할이 불가할때까지의 조건 만들기
    if end - start == 1:

        return start, end # 리스트가 1개 일때 분할이 불가하니 그때까지 분할 하게끔 만들기

    # 재귀 호출 만들기(세마이네임)
    mid = (start + end) // 2 # 분할 하고 병합할때의 기준(중간 위치) 만들기 

    # 분할 할때 왼쪽 범위이며, 정렬을 할수 있도록 시작에서 중간까지의 매개변수 사용
    left_s, left_e = merge_sort(start, mid) 
    # 분할 할때 오른쪽 범위이며, 정렬을 할수 있도록 중간에서 끝까지의 매개변수 사용
    right_s, right_e = merge_sort(mid, end) 

    # 병합전, 왼쪽 마지막 > 오른쪽 마지막이면 카운트
    if arr[left_e - 1] > arr[right_e - 1]:
        cnt += 1

    # 정렬 완료 후, 전체 정렬된 변수 합치기
    merge(left_s, left_e, right_s, right_e)

    # 합치고 나면 정렬 완료
    return start, end 

# 주어진 범위(왼쪽, 오른쪽)를 정렬하는 함수
def merge(left_s, left_e, right_s, right_e): 

    # 왼쪽 배열의 시작 인덱스
    l = left_s 
    # 오른쪽 배열의 시작 인덱스
    r = right_s     
    # 배열 길이
    N = right_e - left_s 

    # 정렬된 배열을 넣을 리스트 만들기(리스트 길이는 배열길이만큼)
    result = [0] * N 
    
    # result 의 위치를 가리키는 인덱스
    idx = 0 
    
    # l == left_e / r == right_e 되기전까지 반복문
    while l < left_e and r < right_e: 
        # 정렬할 왼쪽, 오른쪽이 둘다 남아있는 경우
        # 왼쪽과 오른쪽중에 작은 원소 놓기
        if arr[l] < arr[r]: 
            # 임시 리스트에 넣기(왼쪽)            
            result[idx] = arr[l] 
            # 다음 정렬할 인덱스
            l += 1 
            # 다음에 넣을 result 인덱스
            idx += 1 
        # 오른쪽일 경우 동일
        else:            
            result[idx] = arr[r]
            r += 1 
            idx += 1 

    # 왼쪽/오른쪽 중 정렬이 끝났을 경우
    # 오른쪽만 남았을 경우(오른쪽 정렬)
    while r < right_e: 
        result[idx] = arr[r] 
        r += 1 
        idx += 1 

    # 왼쪽만 남았을 경우(왼쪽 정렬)
    while l < left_e: 
        result[idx] = arr[l] 
        l += 1 
        idx += 1 
    
    for i in range(N):  
        arr[left_s + i] = result[i] 

T = int(input().strip())  
for tc in range(1, T + 1):
    N = int(input().strip())  # 배열 길이
    arr = list(map(int, input().split()))  # 배열
    cnt = 0  # 조건 만족 횟수 카운트
    
    merge_sort(0, N)
    print(f"#{tc} {arr[N // 2]} {cnt}")  
