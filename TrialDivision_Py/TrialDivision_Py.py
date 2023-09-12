
import math

def eratosthenes(n):
    is_prime = [True] * (n + 1)
    primes = []
    is_prime[0] = False
    is_prime[1] = False
    
    for a in range(2, int(math.sqrt(n)) + 1):
        if is_prime[a]:
            for i in range(a + a, n + 1, a):
                is_prime[i] = False
    
    for i in range(n + 1):
        if is_prime[i]:
            primes.append(i)
    
    return primes

def factorization(p, e, primes, n):
    current = n
    i = 0
    while i < len(primes):
        if current % primes[i] == 0:
            if primes[i] in p:
                index = p.index(primes[i])
                e[index] += 1
            else:
                p.append(primes[i])
                e.append(1)
            current //= primes[i]
        else:
            i += 1
            temp = primes[i] * primes[i]
            if temp > current:
                break
    if current > 1:
        p.append(current)
        e.append(1)

if __name__ == "__main__":
    print("MAT361 Fall 2023: Sieve of Eratosthenes & Unique Factorization - Sungmin Moon")
    print ("This program is(or will be) uploaded in https://github.com/Elphior/MAT361_A2.git")
    num = int(input("Enter the number to factorize: "))
    print()
    print("Prime factorization of", num, ":")
    
    primes = eratosthenes(1000000)
    
    p = []
    e = []
    
    factorization(p, e, primes, num)
    print(f"{num}\n= {' * '.join([f'{p[i]}^{e[i]}' for i in range(len(p))])}")
    