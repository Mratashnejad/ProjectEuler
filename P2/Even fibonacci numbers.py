A = 2
fib = 0
result = 2
total = 0

while (result < 4000000):
    total += result
    result = 4*A + fib
    fib = A
    A = result
print(total)
