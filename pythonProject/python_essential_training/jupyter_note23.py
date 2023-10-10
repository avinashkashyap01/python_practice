
def allprimeupto(num):
    primes = [2]
    for number in range(3,num):
        sqrtnum = number ** 0.5
        for factore in primes:
            if number % factore == 0:
                break
            if factore > sqrtnum:
                primes.append(number)
                break
    return primes

print(allprimeupto(100))
print(allprimeupto(1000))
