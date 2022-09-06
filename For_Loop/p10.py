'''
WAP to replace all the space character to underscore in a given string.
#input st = 'east or west python is the best'
'''
def space_char_replacer():
    st = 'east or west python is the best'
    rep_st = ''
    for i in st:
        if i == " ":
            rep_st += '_'
        else:
            rep_st += i
    print(rep_st)
space_char_replacer()