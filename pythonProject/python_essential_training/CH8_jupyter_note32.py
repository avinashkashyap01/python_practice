import time


# Handling Exceptions
# Try/Exept

def causeerror():
    try:
        return 1/0
    except Exception as e:
        return e

print(causeerror())


def causeerror():
    try:
        return 1/0
    except Exception :
        print('There was some sort of error')

print(causeerror())


# Finally

def causeerror():
    try:
        return 1/0
    except Exception :
        print('There was some sort of error')
    finally:
        print('This will always execute')
print(causeerror())



def causeerror():
    try:
        return 1/1
    except Exception :
        print('There was some sort of error')
    finally:
        print('This will always execute')

print(causeerror())



def causeerror():
    start = time.time()
    try:
        time.sleep(0.5)
        return 1/0
    except Exception :
        print('There was some sort of error')
    finally:
        print(f'Function took {time.time() - start} second to execute')
print(causeerror())



# Catching Exception by Type

def causeerror():
    try:
        return 1 + 'a'
    except TypeError :
        print('There was a typr error!')
    except ZeroDivisionError :
        print('There was a zero division error!')
    except Exception :
        print('There was some sort of error!')

print(causeerror())



# Custom Decorators

def handleException(func):
    def wrapper():
        try:
            func()
        except TypeError :
         print('There was a typr error!')
        except ZeroDivisionError :
         print('There was a zero division error!')
        except Exception :
         print('There was some sort of error!')
    return wrapper
@handleException
def causeerror():
    return 1/0
causeerror()



# Raising Exception

@handleException
def raiseerror (n):
    if n == 0:
        raise Exception()
    print(n)
raiseerror()
