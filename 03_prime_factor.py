from itertools import count, imap, ifilter, takewhile
from math import sqrt

TARGET = 600851475143


def primes():
    """Endless prime numbers list"""
    primes = [2]
    for n in count(3, step=2):
        max_prime = sqrt(n)
        if all(imap(
                # If `n % i == 0`, all() returns False - it is not prime number
                lambda i: n % i,
                takewhile(
                    # Check factors lesser than sqrt(n) - some optimization
                    lambda i: i <= max_prime,
                    primes
                )
            )):
            primes.append(n)
            yield n


def main():
    border_value = sqrt(TARGET)
    print "Border = %d" % border_value
    for i in primes():
        if i > border_value:
            break
        if TARGET % i == 0:
            j = i
    print "Max factor = %d" % j


if __name__ == '__main__':
    main()