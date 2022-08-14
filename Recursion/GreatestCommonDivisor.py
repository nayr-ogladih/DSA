"""
step 1: recursive case - the flow
gcd(a,0)=a
gcd(a,b) = gcd(b, a mod b)

step 2: base condition - the stopping criterion
b = 0

step 3: unintentional condition - the constraint
positive integers
convert negative numbers to postive
"""

def gcd(a,b):
    assert int(a) == a and int(b) == b, 'The numbers must be integers only!'
    if a < 0:
        a = -1 * a
    if b < 0:
        b = -1 * b
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

print(gcd(48,1.8))