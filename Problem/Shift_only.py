N = int(input())
A = list(map(int, input().split()))

counter = 0
can_do = True
while True:
    for i in range(N):
        if A[i] % 2 == 1:
            can_do = False

    if not can_do:  # if Falseと同義
        break

    for i in range(N):
        A[i] //= 2

    counter += 1


print(counter)

