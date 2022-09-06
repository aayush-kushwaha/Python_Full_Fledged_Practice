# WAP to check whether the given number is positive or negative. 
def number_indices_checker(a):
    if a > 0:
        return "It is +ve"
    else:
        return "It is -ve"
print(number_indices_checker(int(input("Enter a Number: "))))
