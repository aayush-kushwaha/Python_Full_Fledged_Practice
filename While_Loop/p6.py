'''
WAP to reverse a string without using slicing by using while loop. #Output should be in tuple.
'''
from operator import length_hint
from re import T


a = input("Enter String: ")
rev = ''
t = ()
i = len(a) - 1
while i >= 0:
    rev += a[i]
    i = i - 1
print(rev)
t += (rev,)
print(t)