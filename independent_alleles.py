import math

N = int(input('Please input N : '))
k = int(input('Please input k : '))

def nCr(n, m):
    if n < m:
        x = math.factorial(m) / math.factorial(n) / math.factorial(m-n)
    else:
        x = 1
    return x

probability = [nCr(i, 2**k)*(1/4)**i*(3/4)**(2**k-i) for i in list(range(N, 2**k+1)) ]
print(sum(probability))
