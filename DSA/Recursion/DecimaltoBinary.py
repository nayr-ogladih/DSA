"""
step 1: recursive case - the flow
divide the number by 2
get the integer quotient for the next iteration
get the remainder for the binary digit
f(n) = n mod 2 + 10*f(n/2)
repeat the steps until the quotient is equal to 0

step 2: the base condition - the stopping criterion
n = 0
step 3: the unintentional case - the constraint

"""

def d2b(n):
    assert int(n) == n, 'The parameter must be an integer only'
    if n == 0:
        return 0
    else:
        return n%2 + 10*d2b(int(n/2))

print(d2b(1.2))
