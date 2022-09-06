'''
WAP to find the sum of integer values present only at even index in a given
heterogeneous collection.
#input h = ['apple', 1, 4.5, 3, 4+5j, True, 6, 7, 6.5]
'''
def even_ind_int_sum():
    h = ['apple', 1, 4.5, 3, 4+5j, True, 6, 7, 6.5]
    sum = 0
    for i in range(len(h)):
        if i % 2 == 0:
            if type(h[i]) == int:
                sum += h[i]
    print(sum)
even_ind_int_sum()