N = int(input())
seat = input()

cnt = seat.count('LL')

if cnt <= 1:
    print(len(seat))
else:
    print(len(seat) - cnt + 1)

