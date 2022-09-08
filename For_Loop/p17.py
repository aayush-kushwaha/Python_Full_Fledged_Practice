'''
17. WAP to get the following outputs
#input: st = 'I AM GENIUS'
#output: out = {'I':[1,'I'], 'AM':[2,'MA'], 'GENIUS':[6,'SUINEG'}
'''
st = 'I AM GENIUS'
l_st = st.split()
# print(l_st)
d = {}
for i in l_st:
        rev = i[::-1]
        d[i] = [len(i),rev]
print(d)