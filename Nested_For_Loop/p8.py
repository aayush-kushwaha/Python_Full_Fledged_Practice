'''
8. WAP to get the following output:
#input: a= ['east', 'west', 'north', 'south']
#output: [['east', 'vs', 'west'], ['east', 'vs', 'north'], ['east', 'vs', 'south'], ['west', 'vs', 'north'], ['west', 'vs', 'south'], ['north', 'vs', 'south']]
'''

a= ['east', 'west', 'north', 'south']
out = []
for i in range(len(a)):
    for j in range(len(a)):
        if i != j:
            b = a[i], 'vs', a[j]
            c = a[j], 'vs', a[i]
            if b not in out and c not in out:
                out.append(b)
print(out)