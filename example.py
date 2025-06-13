from tail_recursive import tail_recursive
import sys

sys.set_int_max_str_digits(0)

# no tail recursion, get recursion depth error
def factorial(n):
    if n == 0: return 1
    else: return factorial(n-1) * n

# print(factorial(10000))

# this has tail-recursion syntax, as it uses an accumulator, but it still runs out of memory
def tail_factorial(n, accumulator=1):
    if n == 0: return accumulator
    # why is it `accumulator *n` here and not just `accumulator`? 
    else: return tail_factorial(n-1, accumulator * n)

# print(tail_factorial(10000))

@tail_recursive
def tail_factorial_decorator(n):
    if n == 0:
        return 1
    else: return n * tail_factorial_decorator.tail_call(n - 1)

print(tail_factorial_decorator(10000))