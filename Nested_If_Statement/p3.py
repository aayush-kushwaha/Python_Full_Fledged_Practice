#  WAP to check whether a given string middle letter is upper case or not.
def mid_char_checker(a):
    if len(a) % 2 != 0:
        if "A" <= a[len(a)//2] <= "Z":
            return "UpperCase"
        elif "a" <= a[len(a)//2] <= "z":
            return "LowerCase"
        elif "0" <= a[len(a)//2] <= "9":
            return "Numeric"
        else:
            return "Special Character"
    else:
        return "It is Even lengthed string."
print(mid_char_checker(input("Enter a String: ")))