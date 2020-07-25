#Result: 100/100 Accepted
for tc in range(int(input())):
    n, k = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]

    first = sum(arr)
    second = 0
    for i, el in enumerate(arr):
        if el <= k: second+=el
        else:second+=k
    print(abs(first-second))