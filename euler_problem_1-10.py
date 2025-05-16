# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 18:09:15 2024

@author: Pranav
"""

#Euler problem 1 - Multiples of 3 or 5
def multiplesOf3Or5(number):
    sum = 0
    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
            sum = sum + i
    return sum

print(multiplesOf3Or5(1000))


#Euler problem 2 - Even Fibonacci numbers
def evenfibsum(number):
    fib = [1, 1]
    sum = 0
    while fib[-1] < number:        
        fib.append(fib[-1] + fib[-2])
    for j in fib:
        if j % 2 == 0:
            sum = sum + j
    return sum   
    
print(evenfibsum(4000000))


#Euler problem 3 - Largest prime factor
def largestprimefactor(number):
    t = 0
    max_check = int(number ** 0.5) + 1
    import sympy
    for i in range(2, max_check):
        if number % i == 0 and sympy.isprime(i) and i > t:
            t = i
    return t

print(largestprimefactor(600851475143))


#Euler problem 4 - Largest palindrome product
def largestPalindromeProduct(n):
    t = 0
    for i in range(10**(n-1), 10**n):
        for j in range(10**(n - 1), 10**n):
            if str(i*j) == (str(i*j))[::-1] and i * j > t:
                t = i * j
    return t
    
print(largestPalindromeProduct(3))


#Euler problem 5 - Smallest multiple
def smallestMultiple(n):
    num = n
    while num > n-1:
        for i in range(1, n+1):
            if num % i != 0: 
                break
        num = num + 1
        if i == n:
            break
    return num-1

print(smallestMultiple(20))


#Euler problem 6 - Sum square difference
def sumSquareDiff(n):
    sum_1 = n * (n + 1) / 2 #sum
    sum_2 = (2*n + 1) * (n + 1) * n / 6 #sum of squares
    return int(sum_1**2 - sum_2)
    
print(sumSquareDiff(100))
            

#Euler problem 7 - 10001st prime
def nthPrime(n):
    import sympy
    return sympy.prime(n)
print(nthPrime(10001))


#Euler problem 8 - Largest product in a series
def largestProductSeries(n):
    pr = 1
    t = 0
    td = [7,3,1,6,7,1,7,6,5,3,1,3,3,0,6,2,4,9,1,9,2,2,5,1,1,9,6,7,4,4,2,6,5,7,4,7,4,2,3,5,5,3,4,9,1,9,4,9,3,4,9,6,9,8,3,5,2,0,3,1,2,7,7,4,5,0,6,3,2,6,2,3,9,5,7,8,3,1,8,0,1,6,9,8,4,8,0,1,8,6,9,4,7,8,8,5,1,8,4,3,8,5,8,6,1,5,6,0,7,8,9,1,1,2,9,4,9,4,9,5,4,5,9,5,0,1,7,3,7,9,5,8,3,3,1,9,5,2,8,5,3,2,0,8,8,0,5,5,1,1,1,2,5,4,0,6,9,8,7,4,7,1,5,8,5,2,3,8,6,3,0,5,0,7,1,5,6,9,3,2,9,0,9,6,3,2,9,5,2,2,7,4,4,3,0,4,3,5,5,7,6,6,8,9,6,6,4,8,9,5,0,4,4,5,2,4,4,5,2,3,1,6,1,7,3,1,8,5,6,4,0,3,0,9,8,7,1,1,1,2,1,7,2,2,3,8,3,1,1,3,6,2,2,2,9,8,9,3,4,2,3,3,8,0,3,0,8,1,3,5,3,3,6,2,7,6,6,1,4,2,8,2,8,0,6,4,4,4,4,8,6,6,4,5,2,3,8,7,4,9,3,0,3,5,8,9,0,7,2,9,6,2,9,0,4,9,1,5,6,0,4,4,0,7,7,2,3,9,0,7,1,3,8,1,0,5,1,5,8,5,9,3,0,7,9,6,0,8,6,6,7,0,1,7,2,4,2,7,1,2,1,8,8,3,9,9,8,7,9,7,9,0,8,7,9,2,2,7,4,9,2,1,9,0,1,6,9,9,7,2,0,8,8,8,0,9,3,7,7,6,6,5,7,2,7,3,3,3,0,0,1,0,5,3,3,6,7,8,8,1,2,2,0,2,3,5,4,2,1,8,0,9,7,5,1,2,5,4,5,4,0,5,9,4,7,5,2,2,4,3,5,2,5,8,4,9,0,7,7,1,1,6,7,0,5,5,6,0,1,3,6,0,4,8,3,9,5,8,6,4,4,6,7,0,6,3,2,4,4,1,5,7,2,2,1,5,5,3,9,7,5,3,6,9,7,8,1,7,9,7,7,8,4,6,1,7,4,0,6,4,9,5,5,1,4,9,2,9,0,8,6,2,5,6,9,3,2,1,9,7,8,4,6,8,6,2,2,4,8,2,8,3,9,7,2,2,4,1,3,7,5,6,5,7,0,5,6,0,5,7,4,9,0,2,6,1,4,0,7,9,7,2,9,6,8,6,5,2,4,1,4,5,3,5,1,0,0,4,7,4,8,2,1,6,6,3,7,0,4,8,4,4,0,3,1,9,9,8,9,0,0,0,8,8,9,5,2,4,3,4,5,0,6,5,8,5,4,1,2,2,7,5,8,8,6,6,6,8,8,1,1,6,4,2,7,1,7,1,4,7,9,9,2,4,4,4,2,9,2,8,2,3,0,8,6,3,4,6,5,6,7,4,8,1,3,9,1,9,1,2,3,1,6,2,8,2,4,5,8,6,1,7,8,6,6,4,5,8,3,5,9,1,2,4,5,6,6,5,2,9,4,7,6,5,4,5,6,8,2,8,4,8,9,1,2,8,8,3,1,4,2,6,0,7,6,9,0,0,4,2,2,4,2,1,9,0,2,2,6,7,1,0,5,5,6,2,6,3,2,1,1,1,1,1,0,9,3,7,0,5,4,4,2,1,7,5,0,6,9,4,1,6,5,8,9,6,0,4,0,8,0,7,1,9,8,4,0,3,8,5,0,9,6,2,4,5,5,4,4,4,3,6,2,9,8,1,2,3,0,9,8,7,8,7,9,9,2,7,2,4,4,2,8,4,9,0,9,1,8,8,8,4,5,8,0,1,5,6,1,6,6,0,9,7,9,1,9,1,3,3,8,7,5,4,9,9,2,0,0,5,2,4,0,6,3,6,8,9,9,1,2,5,6,0,7,1,7,6,0,6,0,5,8,8,6,1,1,6,4,6,7,1,0,9,4,0,5,0,7,7,5,4,1,0,0,2,2,5,6,9,8,3,1,5,5,2,0,0,0,5,5,9,3,5,7,2,9,7,2,5,7,1,6,3,6,2,6,9,5,6,1,8,8,2,6,7,0,4,2,8,2,5,2,4,8,3,6,0,0,8,2,3,2,5,7,5,3,0,4,2,0,7,5,2,9,6,3,4,5,0]
    for i in range(len(td) - n + 1):
        for j in range(n):
            pr = pr * td[i+j]
        if pr > t:
            t = pr
        pr = 1 #resetting to 1
    return t
    
print(largestProductSeries(13))


#Euler problem 9 - Special Pythagorean triplet
def Pytrip(n):
    a = 3
    b = 4
    for a in range(3, int((n - 3)/3 + 1)):
        for b in range(4, int((n - 4)/2)):
            if a*a + b*b == (n - a - b)**2:
                return a * b * (n - a - b)

print(Pytrip(1000))


#Euler problem 10 - Summation of primes
def summPrime(n):
    import sympy
    sum = 0
    for i in range(2, n):
        if sympy.isprime(i):
            sum = sum + i
    return sum

print(summPrime(2000000))



























