T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input().split()))

    sum = 0             #시작 값(기준점)

    for i in arr:           #리스트인 arr 안에 원소를 하나씩 넣어서 반복
        sum += i            #리스트안 모든 원소 합

    avr = round(sum / len(arr))   #합한 수를 원소수만큼 나눠 평균값 구하기
    #인풋값에 29라 나와있고 //로 소수점 빼버리면 28이된다. 고로 반올림 round 사용

        
    print(f"#{tc} {avr}")