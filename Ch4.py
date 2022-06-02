
# make number 0~9
a = range(10)
# list(range(10) mean [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(a))

# make list [2, 5, 8]
b = range(2, 10, 3)
print(list(b))


# not tuple
(38)

# tuple
(38,)
38,

# make tuple (2, 5, 8)
print(tuple(b))


# tuple packing : just packing elements
human = (184, 77)
print(human)

# unpacking
height, weight = human
print(height, weight)

# sequence types = list, tuple, range, str, bytes, bytearray

# range function can't connect each other
# print(range(0,10) + range(10,20)) may error occur
# Use list, tuple to connect

# list 3 times
print([0, 10, 20, 30] * 3)
# String 3 times
print('Hey' * 3)

# Arrays.length() = len()
print(len('Hey Buddy'))

# negative index
a = [39, 23, 54, 33, 10]
# a.index = [0, 1, 2, 3, 4]
# a.index = [-5, -4, -3, -2, -1]
print(a[-5])

print(len(a))
# need -1
print(a[len(a)-1])
print(a[-len(a)])


# tuple, range, String = Reading Only
r = range(0, 10, 2)
hello = 'Hello, World'
# You can't write r or hello

# del function
b = [14, 30, 22, 36, 16]
del b[3]
print(b)

# slicing
c = [12, 14, 19, 18, 20]
# c[0], c[1], c[2]
print(c[0:3])
# You can assign over range index c[ 0 : max-1 ]
print(c[0:len(c)])
# c [0 2 4]
print(c[0:5:2])
print(c[:]); print(c[:3]); print(c[2:]);
print(c[1::2])

# slice with assign
d = [10, 20, 30, 40, 50, 60, 70, 80, 90]
d[2:5] = ['a', 'b', 'c']
print(d)

# flexible to slice
e = [10, 20, 30, 40, 50, 60, 70, 80, 90]
e[2:5] = ['a', 'b', 'c', 'd', 'e']
print(e)

# tuple, range, String also edit unable