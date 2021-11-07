m=input('Enter your name: ')
w=['a','e','i','o','u','A','E','I','O','U']
p=''
for i in m:
    for j in w:
        if i==j:
            m=m.replace(i,'')


print(m)
