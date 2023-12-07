def recursion(x):
    while(x!=2):
        # print(x)
        x=x-1
        print(x)
        recursion(x)
        
    

recursion(8)

# @recursion
def sum(x):
    print("Okay")
    return recursion(x) + recursion(x)