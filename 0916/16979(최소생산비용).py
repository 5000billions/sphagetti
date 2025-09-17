T = int(input())
 
# idx : 배정할 열의 인덱스
# selected : 행들의 목록(리스트)
# now_cost : 현재 비용 합
def digit(idx, selected, now_cost):
    global min_cost
 
    #가지치기
    if now_cost >= min_cost:  #만약 현재 비용이 최소비용보다 크면 볼필요 없으니 가지치기
        return
 
    #종료 조건
    if idx == N: # 모든열에 행이 하나씩 배정됐다면
        min_cost = min(min_cost, now_cost)  #현재 비용과 최소비용 중 작은값
        return
 
    #재귀 호출
    for j in range(N):
        #만약 리스트에 j가 존재하지 않으면 방문 하지 않은 것
        if not j in selected:  
            # 리스트에 추가 해준다(방문 구분하기위해)
            selected.append(j)  
            # 새로운 비용 합
            new_cost = now_cost + factory[j][idx]
            # 다음 열로 진행  
            digit(idx + 1, selected, new_cost) 
            #새로운 곳을 탐색하기 위해서는 전에 있던 걸 취소해준다
            selected.pop()  
            
for tc in range(1, T+1):
    N = int(input())
    factory = [list(map(int, input().split())) for _ in range(N)]
    # 최소비용
    min_cost = 10**18 
    # 출발을 0으로 시작, 리스트도 빈리스트, 현재 비용도 0으로 시작 
    digit(0, [], 0)  
    print(f"#{tc} {min_cost}")