#!/usr/bin/env python

def check_prime(x):
    if x % 2 ==0:
        return False
    for i in range(3,x,2):
        if x % i == 0:
            return False
            break
    return True

primes = 0
num = 1

while primes < 10002:
    if check_prime(num):
        primes=primes+1
        if primes == 10001:
            break
    num=num+2
        
print num
   
