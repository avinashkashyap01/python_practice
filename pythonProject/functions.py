
def Funct(number):
    number = number*number
    return number
b=10
h=Funct(b)
c=5
print(b*c)
print(h)

def Funct(hery):
    hery=hery - hery
    return hery
a=45
b=Funct(a)
c=35
print(b)
print(c-a)

def addfive(num):
    num=num+5
    return num
a=30
b=addfive(a)
print(b)

def addhundred(sum):
    sum=sum+100
    return sum
sum=20
a=addhundred(sum)
print(a)

def Funct(bus):
    bus=bus+2
    return bus
bus=5
print(bus)
bus1=bus+5
print(bus1)

def addfive(bus):
    output=bus+5
    return output

bus=0
print(bus)
bus1=addfive(bus)
print(bus1)
bus2=addfive(bus1*10)
print(bus2*10)
bus3=addfive(bus2-50)
print(bus3*10)
bus4=(bus3*50)
print(bus4)

def addfouraddfive(num1,num2):
    output=num1+4
    # output=output+num2+5
    output+=num2+5
    return output
sum = addfouraddfive(3,6)
print(sum)
