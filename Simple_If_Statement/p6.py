# WAP to check whether the given input 1 is present in input 2 or not.
def element_checker():
    Input1 = 'hello'
    Input2 = ['hai','hello','helloo','hai']
    if Input1 in Input2:
        return "It is present in Input 1"
    else:
        return "It is not present in Input 1"
print(element_checker())