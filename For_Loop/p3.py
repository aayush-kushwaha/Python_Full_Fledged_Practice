'''
WAP to print all the vowels character present in the given string.
#input s= 'pRogRAMmInG'
'''
def vowel_char_printer():
    s = 'pRogRAMmInG'
    for i in s:
        if i in 'AEIOUaeiou':
            print(i)
vowel_char_printer()