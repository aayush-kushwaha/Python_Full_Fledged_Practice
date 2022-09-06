#  WAP to check whether the given input is palindrome or not using slicing.
def palindrome_checker(a):
    rev = a[::-1]
    if a == rev:
        return "It is Palindrome"
    else:
        return "it is not Palindrome"
print(palindrome_checker(input("Enter String: ")))
