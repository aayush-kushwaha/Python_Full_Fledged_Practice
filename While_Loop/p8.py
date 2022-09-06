# 8. WAP to print fibonacci series.
n = int(input("Enter the series: "))
a = 0
b = 1
print(a)
print(b)
i = 0
while i <= n:
    c = a + b
    a = b
    b = c
    print(c)
    i += 1