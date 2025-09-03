#1289
T = int(input())
for tc in range(1, T + 1):
    # 메모리 배열로 만들기
    goal = list(input()) 
    # 메모리 길이 구하기
    n = len(goal)

    # 시작 메모리를 목표 메모리 길이 만큼으로 맞춰 초기화하기
    begin = ['0'] * n
    # 목표 메모리까지 만들 횟수 초기화하기
    stack = 0

    # 길이만큼(메모리 비트수 만큼) for문을 돌리기
    for i in range(n):
        # 시작 메모리 비트랑 목표 메모리 비트가 다를 시 
        if begin[i] != goal[i]:
            # 횟수 추가하기
            stack += 1
            # 그 지점부터 목표값으로 맞추기
            fill = goal[i]
            # 위 시작 메모리 넣는 작업을 반복문 만들기 
            for j in range(i, n):
                # 시작 메모리에 넣기
                begin[j] = fill

    print(f"#{tc} {stack}")