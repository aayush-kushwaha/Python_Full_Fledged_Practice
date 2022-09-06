'''
 WAP to remove the duplicate values present in the even index collection and store it in output variable.
#input: 
# p = ('Python', 'BTM_Layout', 'Bengaluru', 'Python', 'July', 10, 20, 10, 200, True, 'True', 'Bengaluru')
'''
p = ('Python', 'BTM_Layout', 'Bengaluru', 'Python', 'July', 10, 20, 10, 200, True, 'True', 'Bengaluru') 
out = ()
for i in range(len(p)):
    if i % 2 == 0:
        if p[i] not in out:
            out += (p[i],)
print(out)