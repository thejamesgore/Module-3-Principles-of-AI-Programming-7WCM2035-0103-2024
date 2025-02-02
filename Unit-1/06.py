def sorting():
    X = ["a","b","c","d","e","f","g","h","i"]
    Y = [0,1,1,0,1,2,2,0,1]
    
    z = [i for _, i in sorted(zip(Y,X))]
    print(z)
    
sorting()