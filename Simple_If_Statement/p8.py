# WAP to check whether the given number is even or not.
def odd_even_checker(a):
    if a % 2 == 0:
        return a,"is even number"
    else:
        return a,"is odd number"
print(odd_even_checker(int(input("Enter a number: "))))
