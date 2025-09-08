
def sudoku(nums):
    # 길이가 9이고 숫자 범위가 1~9이며 중복이 없어야 함
    return sorted(nums) == [1,2,3,4,5,6,7,8,9]

T = int(input().strip())
for tc in range(1, T + 1):
    board = [list(map(int, input().split())) for _ in range(9)]

    ok = 1  # 일단 가능하다고 가정

    # 1) 행 검사(함수 조건에 안맞을시 스도쿠 조건 X 바로 break)
    for r in range(9):
        if not sudoku(board[r]):
            ok = 0
            break

    # 2) 열 검사 (행에서 탈락하지 않았다면)
    if ok:
        for c in range(9):
            col = [board[r][c] for r in range(9)]
            if not sudoku(col):
                ok = 0
                break

    # 3) 3x3 박스 검사
    if ok:
        for sr in range(0, 9, 3):         # 시작 행: 0,3,6
            for sc in range(0, 9, 3):     # 시작 열: 0,3,6
                block = []
                for r in range(sr, sr + 3):
                    for c in range(sc, sc + 3):
                        block.append(board[r][c])
                if not sudoku(block):
                    ok = 0
                    break
            if not ok:
                break

    print(f"#{tc} {ok}")
