''' WAP to check whether the given input is an integer or not. 
Use input statement and output statement in the program.
'''
def type_checker(a):
    if type(a) == int:
        return "It is an integer"
    else:
        return "It is not an integer"
print(type_checker(5))