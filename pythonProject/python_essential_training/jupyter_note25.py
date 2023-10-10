
# Function Scope
def performoperarion(*args,**kwargs):
    print(args)
    print(kwargs)
performoperarion(1,2,3, operation ='sum')


# Locals
# def performoperarion(num1,num2, oparation = 'sum'):
#     print(locals())
# performoperarion(1,2, operation ='multiply')
# print(num1)


# Globals
print(globals())


# Global and Local Scope

massage = 'some global data'
def function1(varA,varB):
    print(massage)
    print(locals())

def function2(varC,varD):
    print(massage)
    print(locals())

function1(1,2)
function2(3,4)



massage = 'some global data'
varA = 2
def function1(varA,varB):
    massage = 'some global data'
    print(varA)
    print(massage)
    print(locals())

def function2(varC,varD):
    print(varA)
    print(massage)
    print(locals())

function1(1,2)
function2(3,4)




def function1(varA,varB):
    massage = 'some global data'
    print(varA)
    def inner_function(varA,varB):
        print(f'inner_function local scope :{locals()}')

    inner_function(123, 456)
function1(1,2)



def function1(varA,varB):
    massage = 'some global data'
    print(varA)
    def inner_function(varA,varB):
        print(f'inner_function local scope :{locals()}')
    print(locals())
    inner_function(123, 456)
function1(1,2)
