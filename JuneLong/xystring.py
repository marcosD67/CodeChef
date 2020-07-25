#Result: 100/100
#Python solution
for tc in range(int(input())):
    students = input()
    students = list(students)
    n = len(students)
    count, i = 0, 0
    while i < n-1:
        if students[i] != students[i+1]: 
            count+=1
            i+=2
        else: i+=1
    print(count)