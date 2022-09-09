'''
7. WAP to get the following output:
#input: a = [2, 3, 1, True, 'hello', 3]
#output: out = [9, 6, 18, 18, 18, 6]
'''
a = [2, 3, 1, True, 'hello', 3]
out = []
for i in range(len(a)):
    p = 1
    for j in range(len(a)):
        if i != j and type(a[j]) == int:
            p *= a[j]
    out.append(p)
print(out)