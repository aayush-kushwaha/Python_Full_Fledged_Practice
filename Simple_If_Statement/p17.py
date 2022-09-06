# WAP to check whether the relation(greater,lesser,or equal) between two given numbers.
def rel_checker(a,b):
    if a > b:
        print(a,"is greater than",b)
    elif a < b:
        print(b,"is greater than",a)
    elif a == b:
        print(a,"is equal to",b)
rel_checker(int(input("Enter first number: ")),int(input("Enter second number: ")))