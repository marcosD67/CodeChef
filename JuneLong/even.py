#Result: 100/100
#print a spiral matrix
for tc in range(int(input())):
    n = int(input())
    matrix = [[0 for i in range(n)] for i in range(n)]
    sizeLeft, bounds = n-1, n-1
    flag = 1
    move = 'r'
    row, col = 0, 0
    for i in range(1, (n*n+1)):
        
        matrix[row][col] = i
        # print(move, end = ' ')
        if move == 'r': 
            col+=1
        elif move == 'l':
            col-=1
        elif move == 'u': 
            row-=1
        elif move == 'd':
            row+=1


        if i == bounds:
            bounds += sizeLeft

            if flag != 2:
                flag = 2
            else:
                flag = 1
                sizeLeft -= 1

            if move == 'r':
                move = 'd'
            elif move == 'd':
                move = 'l'
            elif move == 'l':
                move = 'u'
            elif move == 'u':
                move = 'r'
    
    for x in matrix:
        for el in x:
            print(el, end = ' ')
        print()