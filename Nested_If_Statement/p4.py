''' 
WAP to check whether the given collection is a dictionary or not. 
If the collection is a dictionary then extract all the keys and values in the form of nested tuple.
'''
def collection_checker():
    a = {'Aayush':1728107,'Archana':1728119,'Sonali':1728117,'Souvik':'Lateral Entry'}
    # t = ()
    if type(a) == dict:
        print("It is a dictionary!!")
        # key = a.keys()
        # value = a.values()
        item = a.items()
    # print(key)
    # print(value)
    # t = (key,value)
    print(item)
    # print(t)
collection_checker()