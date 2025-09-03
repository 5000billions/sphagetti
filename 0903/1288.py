T = int(input())
for x in range(1, T + 1):
    N = int(input())

# 본 숫자들을 저장해 둘 공간 만들기(중복되면 안되기에 set사용)
number = set()
# 양을 늘릴 증가시킬 더미 배수 초기화
dummy = 0

# 반복문 끝낼 조건 만들기(0~9인 10개가 모이는 순간 종료)
while len(number) < 10:
    # 반복 될때마다 배수 증가
    dummy += 1
    # 양의수 구하기
    num = N * dummy
    # 문자열로 바꿔서 저장 하기
    number.update(str(num))

print(f"#{x} {num}")