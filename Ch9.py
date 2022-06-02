# [0, 1, 2, 3]
print(list(range(4)))
# 4
print(len(list(range(4))))


# list comprehension
a = [i for i in range(10)]
print(a)

# for value in list
b = list(i for i in range(10))
print(b)

# examples
print([i + 5 for i in range(10)])
print([i * 2 for i in range(10)])
print([i for i in range(10) if i % 2 == 0])
print([i * j for j in range(2,10)
             for i in range(1,10)])
print(list(map(int, [1.2, 2.5, 3.7, 4.6])))

ex1 = [[10, 20], [30, 40], [50,60]]
for x, y in ex1:
    print(x,y)

# append = plus element at last part of array
a= [1, 2]; a.append(3)
print(a)

# copy
b = a.copy()
print(b)
# deepcopy = over 2-dimension array must use deepcopy function, not copy function

# keys, values, items
ExDic1 = {'a':10, 'b':20, 'c':30, 'd':40}
for key in ExDic1.keys():
    print(key, end=' ')

ExDic2 = {'a':10, 'b':20, 'c':30, 'd':40}
for value in ExDic2.values() :
    print(value, end=' ')

ExDic3 = {'a':10, 'b':20, 'c':30, 'd':40}
for item in ExDic3.items() :
    print(item, end=' ')
print()

# if conditional statement in dictionary
# dictionary use if conditional statement instead of statement
ExDic4 = {'a':10, 'b':20, 'c':30, 'd':40}
ExDic4 = {key : value for key, value in ExDic4.items() if value != 20}
print(ExDic4)


