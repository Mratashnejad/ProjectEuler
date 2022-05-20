A = 2
fib = 0
result = 2
total = 0
#fibonacci bellow 4 milion
while (result < 400000):
    total += result
    result = 4*A + fib
    fib = A
    A = result
print(total)
