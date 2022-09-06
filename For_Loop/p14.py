'''
WAP to get the following output.
#Output: ['roses', 'are', 'red']
#Input: st = 'roses are red'
'''
# Using Inbuilt function
def str_to_list1():
    st = 'roses are red'
    l = st.split()
    print(l)
str_to_list1()

# Without using Inbuilt function
'''
def str_to_list2():
    st = 'roses are red'
    st_new = 

    l = []
    for i in st:
        if i == ' ':
            continue
        else:
            l += [i]
    print(l)
str_to_list2()
'''