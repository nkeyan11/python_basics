n=int(input('Enter the first number: '))
m=int(input('Enter the second number: '))
q=0
w=0
for i in range(1,n):
    if n%i==0:
        q=q+i
for j in range(1,m):
    if m%j==0:
        w=w+j
if (q==m) and (w==n):
    print('The given numbers are amicable')
else:
    print('The given numbers are not amicable')
