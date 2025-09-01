T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input().split()))

    sum_odd = 0             #시작 값(기준점)

    for i in arr:           #리스트인 arr 안에 원소를 하나씩 넣어서 반복
        if i % 2 == 1:      #원소중 홀수인 수를 속아내기
            sum_odd += i    #속아낸 홀수들을 sum_odd에 더하기
        
    print(f"#{tc} {sum_odd}")