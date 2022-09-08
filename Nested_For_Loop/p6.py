'''
6. WAP to get the following output.
#input: p = '33344563355644555'
#output: out = '5'
'''
p = '33344563355644555'
count = 0
out=''
for i in p:
    temp=0
    for j in p:
        if i == j:
            temp+=1
    if temp>count:
        count=temp
        out=i
print(out)