
# Functions
import math
def performoperation(num1,num2,operation):
    if operation == 'sum':
        return num1 + num2
    if operation == 'multiply':
        return num1 * num2
print(performoperation(2,5,'sum'))


# Named Parameters

def performoperation(num1,num2,operation = 'sum'):
    if operation == 'sum':
        return num1 + num2
    if operation == 'multiply':
        return num1 * num2
print(performoperation(2,5))


def performoperation(num1,num2,operation = 'sum',message = 'default messege'):
    print(message)
    if operation == 'sum':
        return num1 + num2
    if operation == 'multiply':
        return num1 * num2
print(performoperation(2,5,message='a new message',operation='multiply'))


# *args

def performoperarion(*args):
    print(args)
performoperarion(1,2,3)


# **kwargs
def performoperarion(*args,**kwargs):
    print(args)
    print(kwargs)
performoperarion(1,2,3, operation ='sum')


def performoperation(*args,operation = 'sum'):
    if operation == 'sum':
        return sum(args)
    if operation == 'multiply':
        return math.prod(args)
print(performoperation(1,2,3,4,6,8,operation='sum'))
