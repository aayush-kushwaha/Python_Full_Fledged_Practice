# WAP to check whether the given character is upper case or not without using inbuilt function and inbuilt function.

# Without Inbuilt Function
def Case_Checker(a):
    if "A" <= a <= "Z":
        return "It is UpperCase"
    elif "a" <= a <= "z":
        return "It is LowerCase"
    elif "0" <= a <= "9":
        return "It is Numeric"
    else:
        return "It is Special Character"
print(Case_Checker(input("Enter a character: ")))

# With Inbuilt Function
def Case_Checker2(a):
    if a.isupper():
        return "It is UpperCase"
    elif a.islower():
        return "It is LowerCase"
    elif a.isnumeric():
        return "It is Numeric"
    else:
        return "Special Character"
print(Case_Checker2(input("Enter a character: ")))