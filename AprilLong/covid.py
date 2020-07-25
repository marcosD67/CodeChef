#Result: 100/100 Accepted
for tc in range(int(input())):
    n = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    able = True
    curr = -1
    for i, el in enumerate(arr):
        if el == 1:
            if curr != -1:
                if i - curr < 6:
                    able = False
                    break
            curr = i
    print("YES" if able else "NO")