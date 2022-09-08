'''
3. WAP to print the series of perfect numbers between the range 1 to 1000.
'''
# 3 * 2 = 6 || 1+2+3 = 6
n = int(input("Enter a number: "))
out = 0 
for i in range(1,n):
    if n % i == 0:
        out += i
if out == n:
    print(i)