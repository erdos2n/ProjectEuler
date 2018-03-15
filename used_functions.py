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