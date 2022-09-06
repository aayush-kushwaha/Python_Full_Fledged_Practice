'''
WAP to check whether the given string is having a special character or not.
#input st = 'BTM_PySpiders'
'''
def special_char_checker():
    st = 'BTM_PySpiders'
    for i in st:
        if i.isalnum(): # if "A" <= i <= "z" or "0" <= i <= "9":
            continue
        else:
            print(i,"is special character!!!")
special_char_checker()