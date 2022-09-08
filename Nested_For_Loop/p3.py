'''
3. WAP to print the series of perfect numbers between the range 1 to 1000.
'''
#  6 || 1+2+3 = 6
n=1000
for i in range(1,n+1):
    sum=0
    for j in range(1,i):
        if i%j==0:
            sum+=j
    if i==sum:
        print(i)
