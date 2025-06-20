class Recurse(Exception):
    """
    custom Recurs exception. stores the arguments of the function in the 
    exception object
    """
    def __init__(self, *args, **kwargs):  
        self.args = args
        self.kwargs = kwargs

def recurse(*args, **kwargs):
    """
    instead of calling function recursively, raises a Recurse exception 
    with the new arguments. This interrupts the normal flow & signals to the 
    decorator to recurse with the new arguments
    """
    raise Recurse(*args, **kwargs) 
        
def tail_recursive_v2(f): 
    def decorated(*args, **kwargs): 
        while True: # infinite loop which gets interrupted every time a new Recurse exception is raised 
            try:
                return f(*args, **kwargs) # returns value when base case is reached & no longer calling a function
            except Recurse as r: # unpacks the arguments carried over by raising Recurse
                args = r.args
                kwargs = r.kwargs
                continue
    return decorated  

# @tail_recursive_v2
# def factorial(n, accumulator=1):
#     if n == 0:
#         return accumulator # exit condition
#     recurse(n-1, accumulator=accumulator*n)

# factorial(2)