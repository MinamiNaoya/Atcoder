N = int(input())
L = list(map(int, input().split()))

# 最初に配列を大きいものから順に並び替えておく。
L.sort(reverse=True)
result = 0
for i in range(N):
    if i % 2 == 0:
        result += L[i]

    else:
        result -= L[i]

print(result)



