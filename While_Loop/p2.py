# WAP to print the n series of even numbers. 
def even_no_series():
    a = int(input("Enter upto where you wanna print the series of even no: "))
    i = 0
    while i <= a:
        if i % 2 == 0:
            print(i)
        i += 1
even_no_series()