#Solved after the contest ended. The editorial is very helpful and
#be found here: https://discuss.codechef.com/problems/PTMSSNG

#Result: 100/100 Accepted
#finding the missing point could be done with the bitwise XOR operation
#on all of the x-coordinates and y-coordinates
for tc in range(int(input())):
    n = int(input())
    
    ansX, ansY = 0, 0
    
    for i in range(4*n-1):
        x, y = [int(x) for x in input().split()]
        ansX ^= x
        ansY ^= y
    print(ansX, ansY)