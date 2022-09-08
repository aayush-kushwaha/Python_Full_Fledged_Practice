'''
4. WAP to get the following output.
#input: st = 'aabbcaabccda'
#output: 'a5b3c3d1'
'''
st = 'aabbcaabccda'
out = ''
for i in st:
    count = 0
    for j in st:
        if i == j:
            count += 1
    if i not in (out):
        out += i + str(count)
print(out)