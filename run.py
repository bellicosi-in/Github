def recursion(x):
    while(x!=2):
        # print(x)
    while(x!=2) and x is not None:
        print(x)
        print("recursion")
        x=x-1
        print(x)
        recursion(x)
        
        # while x is not None:

        recursion(x)
        return x
    

recursion(8)

# @recursion
def sum(x):
    print("Okay")
    return recursion(x) + recursion(x)

recursion(recursion(8))
recursion(8)


def run(x):
    print("double recursion")
    if x is not None:
        return recursion(x)+ recursion(x*2)


run(5)
