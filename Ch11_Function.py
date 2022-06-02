def hello():
    # Docstring
    "곱셈하는 함수"
    print('Hello world')

# Call
print(hello())
print(help(hello))

# positional argument
# def fn(a,b,c)

# unpacking
print(*[10, 20, 30])

# variable arguments
def print_number(*args):
    for arg in args:
        print(arg)

def print_3_times(n, *values):
    for i in range(n):
        for value in values:
            print(value)
print(print_3_times(3,'hi', 'bye', 'who'))
# args possessed init value must use behind the args no init value!!!

# use ** store dict form
# * call list form, ** unpacking dict form
def dic_print(**x):
    print(x)

def persnal_info(**data):
    # pass : postpone building functional code
    pass
    # name = input(" 이름을 입력해주세요 : ")
    # age = input(" 나이를 입력해주세요 : ")
    # address = input(" 주소를 입력해주세요 : ")
    # print("이름 " + name)
    # print("나이 " + age)
    # print("주소 " + address)
persnal_info()

# keyword args


# recursive call 재귀 호출
# factorial example
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
print(factorial(5))
