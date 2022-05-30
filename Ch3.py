x = 10
# type imform you type of variable
print(type(x))

x, y = 10, 20
#change each variable's value (aka Dynamic Typing)
x, y = y, x
print(x); print(y)

#delete variable
del x

# empty variable, upper N use
x = None
print(x)

a = 10
#equal a = a + 10  -= *= /= //=
a += 20
print(a)

#split makes received input to Array
# a = input('Type array input : ').split(',')
# print(a)

# map method( input1, input2) make data to input1 data form.

#map equals FloorMethod in java
c = [1.2, 2.5, 30.7, 4.6]
c = list(map(int, c))
print(c)

#sep locate between elementals
print(1,2,3,sep='하고 ')

print(4,5,6,sep='\n')

#end makes input1 contiue writing
print(4,end=' ')
print(5,end=' ')
print(6,end=' 끝')

# escape : To put ' (single quotation marks) in '     '     just /' is useful
