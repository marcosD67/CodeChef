#Result: 100/100
#key was to prioritize giving a 10 coin as change for a 15 over giving
#2 5 coins

from collections import defaultdict
for tc in range(int(input())):
    n = int(input())
    arr = [int(x) for x in input().split()]
    coins = defaultdict(int)
    isAble = True
    for x in arr:
        coins[x]+=1 #add to coin collection
        if x == 5: continue
        elif x == 15: #either can be a 10 or 2 5s
            gaveChange = False
            if coins[10] >= 1: #give them back 1 10 coin
                coins[10] -= 1
                gaveChange = True
            if coins[5] >= 2 and not gaveChange: #give them back 2 5 coins
                coins[5] -= 2
                gaveChange = True
            if not gaveChange:
                isAble = False
        else:
            if coins[5] < 1: isAble = False
            else: coins[5] -= 1
    print("YES" if isAble else "NO")