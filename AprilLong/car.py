#Result: 100/100 Accepted

mod = 10**9+7
for tc in range(int(input())):
    n = int(input())
    arr = [int(x) for x in input().split()]
    total = 0
    for i, el in enumerate(sorted(arr, reverse=True)):
        total = (total + max((el-i), 0)) % mod
    print(total%mod)