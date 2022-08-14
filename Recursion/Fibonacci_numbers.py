"""
Fibonacci sequence is a sequence of numbers in which each number is the sum
of the two preceding ones and the sequence starts from 0 and 1

Step 1: Recursive case - the flow

(5 = 3 + 2): f(n) = f(n-1) + f(n-2)

Step 2: Base Condition - the stopping criterion

0 and 1

Step 3: The unintentional case


"""

def fibonacci(n):
    #unintentional case
    assert n >= 0 and int(n) == n, 'Fibonacci number cannot be negative or non integer number.'
    #base condition:
    if n in [0,1]:
        return n
    else:
        #the flow
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(11))