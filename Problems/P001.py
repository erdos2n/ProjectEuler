def checkfirst(n):
    first10=str(n)[:9]
    return len(set(first10))==9 and '0' not in first10   

def checklast(n):
    last10=str(n%1000000000)
    return len(set(last10))==9 and '0' not in last10

def fib():
    a, b = 0, 1
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b 

if __name__=='__main__':
    for index, i in enumerate(fib()):
        if checkfirst(i) or checklast(i):
            print(index)
        if checkfirst(i) and checklast(i):
            print(index)
            break