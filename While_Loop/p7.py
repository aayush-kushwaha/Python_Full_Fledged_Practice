'''
WAP to reverse the number and check whether the number is palindrome or not
without using typecasting.
'''
num = int(input("Enter a number: "))
rev_num = 0
while num != 0:
    dig = num % 10
    rev_num = rev_num * 10 + dig
    num = num // 10
print(rev_num)


'''
num = 1234
reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print("Reversed Number: " + str(reversed_num))

'''