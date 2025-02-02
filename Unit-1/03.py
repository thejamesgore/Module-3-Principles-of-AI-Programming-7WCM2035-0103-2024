f = [1,2,3,4,5,6,7,8]
g = (2,3,4,5,6,7,8,9)

def access_data(x):
    if x <= len(f)-1:
        print("f ia an", type(f), ", you have selected the ", x, "element which is", f[x])
        print("g ia an", type(g), ", you have selected the ", x, "element which is", g[x])
        
        start = 0
        stop = len(f)
        incr = 1
        
        for i in range(start, stop, incr):
            print("f =", f[i])
        
    else:
        print("x is too big")
        
access_data(3)