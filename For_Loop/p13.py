# WAP to check whether the given number is prime or not.
a = int(input("Enter a number: "))
flag = False
if a > 1:
    for i in range(2,a):
        if a % i == 0:
            flag = True
            break
if flag:
    print(a,"Not a Prime Number")
else:
    print(a,"Prime Number")