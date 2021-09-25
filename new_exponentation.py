import time
import math
from timeit import default_timer as timer

def new_expo(base, exponent):
        if exponent <= 20:
                s = timer()
                r = base ** exponent
                return timer()-s, r
        
        base = base ** 2
        exponent = exponent / 2
        
        return new_expo(base, exponent)


base = 8
exponent = 80

start_time = time.perf_counter()
result = round(math.pow(base, exponent))
print('Time taken by pow in math.pow: {:.15f}'.format(time.perf_counter() - start_time))
print('{:d}'.format(result), end='\n\n')

start_time = time.perf_counter()
result = round(base ** exponent)
print('Time taken by (a ** b) operator: {:.15f}'.format(time.perf_counter() - start_time))
print('{:d}'.format(result), end='\n\n')

while exponent >= 20:
        base = base ** 2
        exponent = exponent / 2

stime = time.perf_counter()
result = round(base ** exponent)
print('Time taken by new_expo function: {:.15f}'.format(time.perf_counter() - stime))
print('{:d}'.format(result))
