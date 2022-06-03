# try exception else finally
def example_try_exception():
    y = list(range(10,40,10))
    try:
        index, x = map(int, input('인덱스와 나눌숫자를 입력하세요 : ').split())
        print(y[index] / x)
    except ZeroDivisionError as e:
        print("0으로 나눌순 없습니다",e)
    except ValueError:
        print("다시 입력하세요")
        example_try_exception()
    else :
        pass
    finally:
        print("END!")
# example_try_exception()

# raise
def multiful_3():
    try :
        x = int(input('3의 배수를 입력하세요 : '))
        if x % 3 != 0:
            raise Exception('3의 배수가 아닙니다')
        print(x)
    # except error type1 :
    #     pass
    # except error type2 :
    #     pass
# Excetpion cover possible all error except writing error type
# so writing end of try catch grammer
    except Exception as e :
        print("예외발생",e)
# multiful_3()


# Making exception
class Not3multipleError(Exception):
    def __init__(self):
        super().__init__('3의 배수가 아닙니다')
def mul3():
    try:
        x = int(input('3의 배수를 입력하세요'))
        if x % 3 != 0:
            raise Not3multipleError
        print(x)
    except Exception as e:
        print('예외가 발생했습니다',e)
mul3()