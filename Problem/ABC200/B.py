N, K = map(int, input().split())
i = 0
while i < K:
    i += 1
    if N % 200 == 0:
        N //= 200
    else:
        string = "".join([str(N), "200"])
        N = int(string)

print(N)