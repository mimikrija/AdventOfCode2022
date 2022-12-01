
from santas_little_helpers.helpers import *

data = get_input('inputs/01.txt', True)

def f(x):
    return True

# sum by condition
print(sum(num for num in data if f(num)))

# count satisfying conditions
print(sum(f(num) for  num in data))
