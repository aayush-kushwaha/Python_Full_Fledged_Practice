'''
5. WAP to get the sum of integers present in a nested list value in a given
collection.
k = [4.5, 3.5, [10,4.5,20],5,6,[1,2,5,9.5,[3,4,9.5,6.5]],4.5]
'''
k = [4.5, 3.5, [10,4.5,20],5,6,[1,2,5,9.5,[3,4,9.5,6.5]],4.5]
def sam():
sum = 0
# static
for i in k:
    if type(i) == list:
        for j in i:
            if type(j) == list:
                for k in j:
                    if type(k) == int:
                        sum += k
            else:
                if type(j) == int:
                    sum += j
print(sum)
sam()

#dynamic

def sum_count(k,out=0):
    for i in k:
        if type(i)==int:
            out+=i
        elif type(i)==list:
            out+=sum_count(i)
        else:
            continue
    return out
print(sum_count(k))

