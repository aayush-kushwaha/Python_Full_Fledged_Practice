'''
1. WAP to print the smallest divisior of the given number using break statement.
'''
def smallest_div(n):
    for i in range(2,n):
        if n % i == 0:
            print(i)
            break
smallest_div(int(input("Enter a number: ")))