#Problem 1
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.
multiples = 0
for i in range(1, 10000):
    if i % 3 == 0:
        #عدد قابل تقسیم به عدد 3 است 111
        print("Number is divided to 3 =" , i)
        multiples += i
    elif i % 5 == 0:
        #عدد قابل تقسیم به عدد 5 است asd
        print("Number is divided to 5 =", i)
        
        multiples += i
print ("Suum of Natural numbers below 10 is :" ,  multiples)
