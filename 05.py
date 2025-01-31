def using_enumerate():
    L = ['apples','bananas', 'oranges']
    for idx, val in enumerate(L):
        print("index is %d and value is %s" % (idx, val))
        
using_enumerate()