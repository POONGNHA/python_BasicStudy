# String change
String1 = 'Hello, world!'
print(String1.replace('world', 'python'))

# upper, lower
print(String1.upper())
print(String1.lower())

# rstrip, lstrip, strip : remove space (left, right)
# strip('to be removed String') : remove only side of String
print(String1.strip('!'))
print(String1.strip('H'))

# just() : make String indicated length
# center() : just() and sort center, if center() didn't matching String length, plus one blank at left side
print(String1.ljust(20))
print(String1.rjust(20))
print('ABC'.center(10))

# Sort by :<  :>
print('{0:<10}'.format('ABCD'))
print('{0:>10}'.format('ABCD'))
print('{0:1<10}'.format(55))
print("{0: >10}".format(15))
# examples
print('%03d' % 1)
print('{0:03d}'.format(35))
print('%08.2f' % 3.6)
print('{0:08.2f}'.format(150.37))

# zfill : fill up zeros
print('35'.zfill(20))

# find : find String and return index left to right
# rfind : the opposite find (right to left)
print('apple juice juice'.find('ju'))

# count : find String using frequency
print('apple juice juice'.count('ju'))


# str.maketrans(To be replaced String, new String), translate
table = str.maketrans('abcde', '12345')
print('apple'.translate(table))

# split(delimiter) : Make list from String
print('apple pear grape pineapple orange'.split())

# join : cut in technique
print(' 007 '.join(['apple', 'pear', 'grape', 'pineapple', 'orange']))

# method chaining
# print(input("Typing plz : ").split())

# format specifier [서식 구분자]
# %s : string, %d : decimal integer (십진 정수), %f : fixed point (고정 소숫점)
# % + number + s : make String length by number and fill blink surplus space
print('%20s' % 'python')
print('%-20s' % 'python')
print('Today is %d %s.' % (4, 'April'))

# formatting method
print('Hello, {0}, {2}, {1}'.format('python', 'Script', 3.0))

# you can designate name instead of index
print('Hello, {language} {version}'.format(language = 'python', version = 3.0))

# f + ' ' = declaration Using format
a1 = 'Good'
b1 = 'night ' + str(33) + ' day'
print(f'hello, {a1}{b1}')

# repeat ',' with 1000 unit number
money = 98178109
print(format(money, ','))