'''
1. WAP to print the series of prime numbers between the range 1 to 20.
'''
def prime_no_series():
    for i in range(1,21):
        ind = 0 
        for j in range(2,i):
            if i % j == 0:
                ind = 1
        if ind == 0:
            print(i)
prime_no_series()