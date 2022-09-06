'''
WAP to extract all the special characters present in a given string.
#input st = 'BTM_PySpiders@'
'''
def special_char_extractor():
    st = 'BTM_PySpiders@'
    out = ''
    for i in st:
        if "A" <= i <= "Z" or "a" <= i <= "z" or "0" <= i <= "9":
            pass
        else:
            out += i
    print(out)
special_char_extractor()