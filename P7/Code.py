# Project Euler Solotion 7


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
  
    
  
