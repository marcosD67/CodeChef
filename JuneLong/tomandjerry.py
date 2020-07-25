#Result: 100/100
#Solution was keep dividing the number by 2
#until it wasn't even anymore. As if the number was odd, then every even number
#would win the game
for tc in range(int(input())):
    n = int(input())
    while n >= 1:
        if n % 2 != 0: #if number is no longer even
            print(n//2) #then all evens before this odd number is the ans
            break
        else:
            n //=2 #keep dividing while number is even