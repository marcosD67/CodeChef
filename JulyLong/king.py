#Result: 100/100 Accpted

#Problem sounded complex, but could be simplified into printing all the
#k empty spaces then the rest of all Xs
''' example:
k = 8 spaces the king needs to reach

key:
O = king
. = empty space
X = blocked space

valid answer:
 O.......
 .XXXXXXX
 XXXXXXXX
 XXXXXXXX
 XXXXXXXX
 XXXXXXXX
 XXXXXXXX
 XXXXXXXX

This works for any k so the problem is simplified to simple printing
'''
for tc in range(int(input())):
    n = int(input())

    for i in range(8):
        for j in range(8):
            if i == 0 and j == 0:
                print("O", end='')
                n-=1
                continue
            if n:
                print(".", end= '')
                n-=1
            else: print("X", end='')
        print()