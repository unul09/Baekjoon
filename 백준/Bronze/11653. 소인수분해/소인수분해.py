n = int(input())

def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return i
    return n


while n != 1:
    div_prime = isPrime(n)
    print(div_prime)
    n //= div_prime