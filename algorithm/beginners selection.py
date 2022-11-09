stdin = int(input())
if stdin < 60:
    print("21:" + str(stdin))
elif 60 <= stdin <= 69:
    print("22:0" + str(stdin-60))
else:
    print("22:" + str(stdin-60))


