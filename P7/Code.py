# Project Euler Solotion 7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

def prime(x):
  primes = [2]
  y = 3
  while len(primes < x):
    for i in primes:
      if i > int(y ** 0.5) + 1:
        primes.append(y)
        break
      if y % i == 0:
        break
     y += 2
   return primes[-1]



print(prime(10001))
  
    
  
