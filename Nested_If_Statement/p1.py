# WAP to check whether the given number is a single digit or double digit or triple digit or more than triple digit.
def digit_checker(a):
    if a >= 0 and a <= 9:
        return "It is Single Digit"
    elif a >= 10 and a <= 99:
        return "It is Double Digit"
    elif a >= 100 and a <= 999:
        return "It is Triple Digit"
    else:
        return "It is more than 3 digit"
print(digit_checker(int(input("Enter a number: "))))
