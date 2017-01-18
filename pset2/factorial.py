# Define a procedure, factorial, that
# takes one number as its input
# and returns the factorial of
# that number.

def factorial(n):
    p = n - 1
    total_sum = 1
    while p > -1:
        sum = 0
        sum = n - p
        total_sum = total_sum * sum
        p = p - 1 
    return total_sum


print factorial(4)
#>>> 24
print factorial(5)
#>>> 120
print factorial(6)
#>>> 720

