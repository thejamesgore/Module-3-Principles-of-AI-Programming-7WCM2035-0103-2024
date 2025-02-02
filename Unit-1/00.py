a = 4
b = 5.3
c = True
d = "some text"
e = {1,2,3,3,3,3,3,3}
f = [1,2,3,4,5,6,7]
g = (2,3,4,5,6,5,3)

def variable_types(x):
    print("Print_variables function")
    print("a ia an", type(a), "and =", a)
    print("b ia an", type(b), "and =", b)
    print("c ia an", type(c), "and =", c)
    print("d ia an", type(d), ", has a length of", len(d), "and =", d)
    print("d ia an", type(e), ", has a length of", len(e), "and =", e)
    print("d ia an", type(f), ", has a length of", len(f), "and =", f)
    print("d ia an", type(g), ", has a length of", len(g), "and =", g)

variable_types("calling with an argument")