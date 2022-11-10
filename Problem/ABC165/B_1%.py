X = int(input())

money = 100
year = 0
while money < X:
    year += 1
    money *= 1.01
    if money >= X:
        print(year)

