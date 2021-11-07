p=int(input('Enter the principal amount: '))
i=int(input('Enter the interest in %: '))
t=int(input('Enter the time of investment(in years): '))
i=i/100
f=p*((1+(i/12))**(12*t))
f=round(f,2)

print('The investment balance after ',t,' years is ',f)
print('The total interest earned is: ',round((f-p),2))
