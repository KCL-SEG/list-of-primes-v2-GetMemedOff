def primeCheck(numIn):
    isPrime = True
    for num in range(2, numIn):
        if numIn % num == 0:
            isPrime = False
    return isPrime


def primes(number_of_primes):
    list = []
    count = 2
    primeCount = 0
    if(number_of_primes <= 0):
        raise ValueError('Invalid number inputted')

    while(number_of_primes > primeCount):
        if(primeCheck(count)):
            list.append(count)
            primeCount += 1
        count += 1
    return list
