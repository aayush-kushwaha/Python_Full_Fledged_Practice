'''
WAP to extract all the uppercase character present in a given string.
#input s= 'pRogRAMmInG'
'''
def uppercase_extractor():
    s = 'pRogRAMmInG'
    out = ''
    for i in s:
        if "A" <= i <= "Z":
            out += i
    print(out)
uppercase_extractor()