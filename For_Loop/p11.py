'''
WAP to extract all the even lengthed string present in a given tuple.
#input p = ('east', 'or', 'west', 'python', 'is', 'the', 'best')
#Output will be in tuple
'''
def even_len_str_extractor():
    p = ('east', 'or', 'west', 'python', 'is', 'the', 'best')
    t = ()
    for i in p:
        if len(i) % 2 == 0:
            t += (i,)
    print(t)
even_len_str_extractor()