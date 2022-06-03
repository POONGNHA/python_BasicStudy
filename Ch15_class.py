class Person:
    # self mean itself
    # instance will place at self's space
    def __init__(self, name, age, address):
        self.hello = 'hi'
        self.name = name
        self.age = age
        self.address = address

    def greeting(self):
        print('{0} 저는 {1} 입니다'.format(self.hello, self.name))


maria = Person('maria', 20, 'seoul')
maria.greeting()

print('name : ', maria.name)

class Personkw :
    def __init__(self,**kwargs):
        self.name = kwargs['name']
        self.age =  kwargs['age']
        self.address =  kwargs['address']

        # __ => private
        self.__wallet = kwargs['wallet']

class Student:
    def __init__(self, name = None, age = 0):
        self.__name = name
        self.__age = age
    # getter : return instance value
    def getAge(self):
        return self.__age
    # setter : set instance value
    def getName(self):
        return self.__name
    def setAge(self):
        return self.__age
    def setName(self):
        return self.__name
prog_stu = Student("hong", 20)
print(prog_stu.getName())
print(prog_stu.getAge())
