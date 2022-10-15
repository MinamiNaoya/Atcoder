def how_many_times(num):
    counter = 0

    while num % 2 == 0:
        num //= 2

        counter += 1

    return counter


N = int(input())
A = list(map(int, input().split()))


INF = 2 ** 30
result = INF

for a in A:
    counter = how_many_times(a)

    result = min(result, counter)
print(result)
