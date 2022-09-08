'''
2. WAP to check whether the given number is prime or not using break statement.
'''
def prime_no_checker(n):
    for i in range(2,n):
        if n % i == 0:
            print("Not a prime Number")
            break
        else:
            print("Prime Number")
            break
prime_no_checker(int(input("Enter a number: ")))