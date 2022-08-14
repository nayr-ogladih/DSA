"""
Step 1: the flow
"""


def sumofDigits(n):
    assert n >= 0 and int(n) == n, 'The number must be postive integer only!'
    if n == 0:
        return 0
    else:
        return int(n % 10) + sumofDigits(int(n//10))

print(sumofDigits(123455555555))
