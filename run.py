def recursion(x):
    while(x!=2):
        print(x)
        print("recursion")
        x=x-1
        # while x is not None:

        recursion(x)
        return x
    


recursion(8)


def run(x):
    print("double recursion")
    if x is not None:
        return recursion(x)+ recursion(x*2)


run(5)