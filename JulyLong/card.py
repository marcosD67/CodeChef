#Result: 100/100 Accepted

for tc in range(int(input())):
    n = int(input())
    chef, morty = 0, 0

    for i in range(n):
        card1, card2 = [int(x) for x in input().split()]
        total1, total2 = 0, 0
        while card1:
            total1 += card1%10
            card1 //= 10
        while card2:
            total2 += card2%10
            card2//=10
        if total1 > total2:
            chef+=1
        elif total1 < total2:
            morty+=1
        else:
            chef, morty = chef+1, morty+1
    if chef == morty:
        print(2, chef) #either score wins
    elif chef > morty:
        print(0, chef) #chef wins
    elif chef < morty:
        print(1, morty) #morty wins