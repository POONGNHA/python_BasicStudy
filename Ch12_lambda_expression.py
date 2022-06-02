# lambda = Function expression limited 1 line code

# lambda examples
print((lambda  x : x +10)(1))
print(list(map(lambda x: x+10, [1, 2, 3])))
a = list(range(1,11))
print(list(map(lambda x: str(x) if x % 3 == 0 else x, a)))

def f(x) :
    return x > 5 and x <9
list1 = list(range(10))
print(list(filter(f,list1)))

# reduce sum all elements in list
a = list(range(1,6))
from functools import reduce
print(reduce(lambda x,y : x+y, a))

# Sorted
animals_list = [('lion', 58), ('cheetah', 200), ('zeebra', 60), ('mooth', 50)]
fast_list = sorted(animals_list, key = lambda ani:ani[1], reverse= True)
for i in fast_list:
    print(i)
