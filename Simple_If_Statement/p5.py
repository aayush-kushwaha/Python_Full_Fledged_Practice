# WAP to check whether the given data is collection or not.
def collection_checker():
    a = [1,2,3,4,5,6,7,8,9,10]
    if type(a) in (str,list,tuple,set,dict):
        return "It is a collection"
    else:
        return "It is not a collection"
print(collection_checker())
