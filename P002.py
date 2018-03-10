from used_functions import *

even_sum=0

for index, i in enumerate(fibonacci_generator()):
    if i%2==0:
        even_sum+=i
    if i>4000000:
        break
print(even_sum)
