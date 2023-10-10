
import random
import time
servicesareup = True

def getdata50():
    if servicesareup and random.random() < 0.5:
        return 'you got the data! that only happens 50% of the time!'

def getdata25():
    if servicesareup and random.random() < 0.25:
        return 'you got the data! that only happens 25% of the time!'

def getdata10():
    if servicesareup and random.random() < 0.1:
        return 'you got the data! that only happens 10% of the time!'

def getwithretry(datafunc):
    maxretries = 20
    for _ in range(0,maxretries):
        responce = datafunc()
        if responce:
            return responce

def getwithretry(datafunc,retries=20):
    if retries == 0:
        return 'THE SERVICE IS DOWN!'
    return datafunc() or getwithretry(datafunc,retries-1)
print(getwithretry(getdata50))
print(getwithretry(getdata25))
print(getwithretry(getdata10))

servicesareup = False
print(getwithretry(getdata50))
print(getwithretry(getdata25))
print(getwithretry(getdata10))




def getdata50():
    time.sleep(.1)
    if servicesareup and random.random() < 0.5:
        return 'you got the data! that only happens 50% of the time!'

def getdata25():
    time.sleep(.1)
    if servicesareup and random.random() < 0.25:
        return 'you got the data! that only happens 25% of the time!'

def getdata10():
    time.sleep(.1)
    if servicesareup and random.random() < 0.1:
        return 'you got the data! that only happens 10% of the time!'

servicesareup = True

print(getwithretry(getdata50))
print(getwithretry(getdata25))
print(getwithretry(getdata10))

servicesareup = False
print(getwithretry(getdata50))
print(getwithretry(getdata25))
print(getwithretry(getdata10))
