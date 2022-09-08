'''
2. WAP to get the following output from the given input:
#input: v = ['apple', 'banana', 'mango', 'grapes', 'orange']
#output: {'apple':2, 'banana':3, 'mango':2, 'grapes':2, 'orange':3}
'''
v = ['apple', 'banana', 'mango', 'grapes', 'orange']
d = {}
for i in v:
    count = 0
    for j in i:
        if j in 'AEIOUaeiou':
            count += 1
    d[i] = count
print(d)
