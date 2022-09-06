''' 
WAP to check whether the given number is divisible by 3 and 5 or not. 
If it is divisible by 3 print 'fizz' and if it is divisible by 5 print 'buzz' 
and if it is divisible by both print 'fizzbuzz'.
'''
def fizzbuzz():
    for i in range(1,51):
        if i % 3 == 0 and i % 5 == 0:
            print (i,"FizzBuzz")
        elif i % 3 == 0:
            print (i,"Fizz")
        elif i % 5 == 0:
            print (i,"Buzz")
fizzbuzz()