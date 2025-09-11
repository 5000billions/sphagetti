T = int(input())
for x in range(1, T + 1):
    N, Q = map(int, input().split())
    arr = [0] * N

    for i in range(1, Q + 1):
        L, R = map(int, input().split())
        if i == 1:
            for r in range(L - 1, R + 1):
                arr[r] = i
        else:
            for c in range(L - 1, R ):
                arr[c] = i    

    print(f"#{x}", *arr)