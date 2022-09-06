#  WAP to print the n series of whole numbers. #Take user input for this.
from re import I


def whole_num_series():
    a = int(input("Enter upto how much series you want to print the whole num: "))
    i = 0
    while i <= a:
        print(i)
        i += 1
whole_num_series()