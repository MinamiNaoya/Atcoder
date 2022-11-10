import math
N, D = map(int, input().split())
xy = [map(int, input().split()) for _ in range(N)]
x, y = [list(i) for i in zip(*xy)]

count = 0
for i in range(N):

    r2 = x[i]**2 + y[i]**2
    r = math.sqrt(int(r2))
    if r <= D:
        count += 1
print(count)