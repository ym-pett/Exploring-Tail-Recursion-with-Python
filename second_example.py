import sys
sys.set_int_max_str_digits(0)

from tail_recursion_v2 import tail_recursive_v2, recurse

# Normal recursion depth maxes out at 980, this one works indefinitely
@tail_recursive_v2
def factorial(n, accumulator=1):
    if n == 0:
        return accumulator
    recurse(n-1, accumulator=accumulator*n)

print(factorial(10000))