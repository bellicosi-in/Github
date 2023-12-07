def recursion(x):
    while(x!=2) and x is not None:
        print(x)
        x=x-1
        return recursion(x)
    


recursion(recursion(8))