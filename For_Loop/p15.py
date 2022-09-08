'''
WAP to check whether the given string is having any vowels or not. If it has any
vowels extract it as a list collection.
#Take user Input
'''
def vowel():
    a = input("Enter String: ")
    l = []
    for i in a:
        if i in "AEIOUaeiou":
            l.append(i)
    print(l)
vowel()