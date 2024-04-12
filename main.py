import math, time

def SieveOfEratosthenes(n):
    # Start time of the function
    startTime = time.time()
    # When to stop looking for the primes
    end = n + 1
    # Bool array making all the elements false for n numbers
    # All numbers are initialized as prime
    composite = [False] * end
    # Goes up to the square root of end + 2 because multiplication is commutative (a * b = b * a)
    for i in range(3, int(end ** 0.5 + 2.01)):
        # If the current number is set to false, or indicated as a prime number
        if not composite[i]:
            # This loop removes all multiples of the current number and will repeat up to the sqrt(end)
            for j in range(i * i, end, i):
                composite[j] = True
    result = [2] + [i for i in range(3, end, 2) if not composite[i]]
    endTime = time.time()
    print("Sieve of Eratosthenes:", endTime - startTime)
    return result


def TrialDivisionCheck(n):
    # Nums < 2 are not prime
    startTime = time.time()
    if n < 2:
        return False
    # 2 and 3 are prime so we can get those out of the way
    if n == 2 or n == 3:
        return True
    # Any multiples of 2 or 3 are also not prime
    if n % 2 == 0 or n % 3 == 0:
        return False

    max = int(math.sqrt(n)) + 1
    # Loops from 5, and goes to the square root of n + 1 counting by 6
    for i in range(5, max, 6):
        # If the input number (potential prime) is divisible by any of the iterators, it is not prime
        # If the number is divisible by that same i + 2 then it is also not prime
        if n % i == 0 or n % (i + 2) == 0:
            return False

    endTime = time.time()
    #print("Time for checking prime:",endTime - startTime)
    # If it has not been marked as not prime earlier, then it is prime
    return True

def TrialDivisionGeneration(n):
    # Get the start time of the algorithm
    startTime = time.time()
    # Array for storing all the prime numbers
    primes = []
    # checks all numbers from 2 to n
    for num in range(2, n + 1):
        # Plugs the number into the trial by division algorithm
        if TrialDivisionCheck(num):
            primes.append(num)
    # get the end time
    endTime = time.time()
    print("Trial Division:", endTime - startTime)
    return primes


n = 5_000_000
TrialByDivisionGeneration(n)
SieveOfEratosthenes(n)
