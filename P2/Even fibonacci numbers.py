fib = 0
a = 0
b = 1
counter = 0
total =0

if fib <= 400000:
    for i in range(1, 500000):
        fib = a + b
        a = b
        b = fib
        print (fib)
    if fib % 2 == 0:
        total +=fib
        print(total)
