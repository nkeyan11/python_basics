p=int(input('Enter the loan amount: '))
i=int(input('Enter the interest in %: '))
n=int(input('Enter the number of installments: '))
i=i/(12*100)
e=(p*i*((1+i)**n))/((1+i)**(n-1))

print(round(e,2))
