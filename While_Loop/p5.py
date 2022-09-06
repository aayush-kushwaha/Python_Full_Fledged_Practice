'''
WAP to find the sum of values present in a given list only if the values are even. 
k = [1,2,3,4,5]
'''
def even_ind_sum():
    k = [1,2,3,4,5]
    sum = 0
    for i in k:
        if i % 2 == 0:
            sum += i
    print(sum)
even_ind_sum()