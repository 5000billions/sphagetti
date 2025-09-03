T = int(input())
for tc in range(1, T + 1):
    N = int(input())

# 소인수 분해할 인수들 리스트로 만들기
cow_human_num = [2, 3, 5, 7, 11]
# 인수들이 사용된 횟수 넣을 리스트 만들기
human_num = []

# 인수들을 하나씩 넣으면서 반복
for chn in cow_human_num:
    # 새로운 반복할때 마다 카운트 초기화(for 밖에 꺼내 놓으면 누적합으로 되어서 안된다.)
    count = 0
    # 나머지가 0일때마다 나눈다.(=나누어 떨어진다)
    while N % chn == 0:
        count += 1
        # 나눈후 몫을 다시 배정
        N //= chn
    # 끝난 인수 별로 위에 빈리스트에 추가
    human_num.append(count)

print(f"#{tc}", *human_num)