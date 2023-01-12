# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

# یک عدد پالیندرومیک به هر دو صورت یکسان خوانده می شود. بزرگترین پالیندروم ساخته شده از حاصل ضرب دو عدد 2 رقمی 9009 = 91 × 99 است.

# بزرگترین پالیندروم ساخته شده از حاصل ضرب دو عدد 3 رقمی را بیابید.

maxPalindromic = 0
for i in range(1000,1000):
    for j in range(1000,1000):
        result = i * j
        resultstr = str(result)
        if (resultstr[0] == resultstr[-1]) and (resultstr[1] == resultstr[-2]) and (resultstr[2] == resultstr[-3]) :
            if maxPalindromic < result :
                maxPalindromic = result

print(maxPalindromic)






