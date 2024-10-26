# x=-5
# if x<0:
#     raise Exception('x should be positive')

# x=5
# assert(x>=0),'x is not positive'

# try:
#     a=5/0
# except Exception as e :
#     print(e)

# try:
#     a=5/0
#     b=a+ '10'
# except ZeroDivisionError as e :
#     print(e)
# except TypeError as e:
#     print(e)
# else:
#     print('everything is fine')

# try:
#     a=5/1
#     b=a+ 4
# except ZeroDivisionError as e :
#     print(e)
# except TypeError as e:
#     print(e)
# else:
#     print('everything is fine')
# finally:
#     print('cleaning up') # finally is always run

class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self,message,value):
        self.message=message
        self.value=value

def test_value(x):
    if x>100:
        raise ValueTooHighError('value is high')
    if x<5:
        raise ValueTooSmallError('Value is small',x)

try :
    test_value(1)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e)
finally:
    print('Completed')
