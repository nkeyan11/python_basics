n=int(input('Enter the starting number: '))
m=int(input('Enter the ending number: '))
for i in range(n,m+1):
    for j in range(2,i):
        if (i%j==0):
            print(i, 'is not a prime number as it is divisible by ',j)
            break
    else:
        print(i,' is a prime number')
            


   
    
