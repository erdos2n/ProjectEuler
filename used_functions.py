def prime_factor_list(n):
    p = [2]
    current_prime = 2
    while n > 1:
        if n % current_prime == 0:
            n //= current_prime
            if current_prime not in p:
                p.append(current_prime)
        else:
            current_prime += 1
    return p


def fibonacci_generator():
    a, b = 0, 1
    yield a
    yield b
    while True:
        a, b = b, a+b
        yield b


def prime_list(n):
    prime_list = [2]
    attempt = 3
    while len(prime_list) < n:
        if all(attempt % i != 0 for i in prime_list):
            prime_list.append(attempt)
        attempt += 2
    return prime_list

def is_prime(n):
    check=int(n**0.5)+1
    isPrime=True
    for i in range(2, check):
        if n%i==0:
            isPrime=False
            break
    return isPrime

def factor_list(n):
    factor_list=[]
    check=int(n**0.5)+1
    for i in range(1, check):
        if n%i==0:
            factor_list.extend([i, int(n/i)])
    return sorted(set(factor_list))

def triangle_number_generator():
    a=1
    b=2
    while True:
        a, b = b+a, b+1
        yield a

def collatz_chain(n):
    steps=0
    while n!=1:
        if n%2==0: 
            n//=2
        else:
            n=3*n+1
        steps+=1
    return steps

def max_sum(triangle):
    while len(triangle) > 1:
        r0 = triangle.pop()
        r1 = triangle.pop()
        triangle.append([max(r0[i], r0[i+1]) + n for i,n in enumerate(r1)])
    return triangle[0][0]

def get_max_sum(filename=''):
    f = [[int(i) for i in row.split(' ')] for row in open(filename).read().split('\n')]
    return max_sum(f)