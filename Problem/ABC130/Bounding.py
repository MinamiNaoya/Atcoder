N, X = map(int, input().split())
L = list(map(int, input().split()))
y_origin = 0
count = 0

for i in range(N):
    y_origin += L[i]
    if y_origin <= X:
        count += 1
    else:
        break
print(count+1)





