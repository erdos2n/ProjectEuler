def prime_factor_list(n):
    p=[2]
    current_prime=2
    while n>1:
        if n%current_prime==0:
            n//=current_prime
            if current_prime not in p: p.append(current_prime)
        else: current_prime+=1
    return p
    
def fibonacci_generator():
    a, b = 0, 1
    yield a
    yield b
    while True:
        a, b = b, a+b
        yield b
