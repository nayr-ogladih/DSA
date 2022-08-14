"""
1) recursive case - the flow
x^n = x*x^(n-1)
2) base condition - the stopping criterion
n = 0
n = 1
3) unintentional condition - the constraint
power(-1,2)
power(3.2,2)
power(2,-1)
"""

def power(base,exponent): 
    assert exponent >= 0 and int(exponent) == exponent, 'The exponent must be positive integer only!'
    if exponent == 0:
        return 1
    elif exponent == 1:
        return base
    return base * power(base,exponent-1) 

print(power(2,-1))
