def recursion(x):
    while(x!=2):
        print(x)
        x=x-1
        return recursion(x)
    

recursion(8)