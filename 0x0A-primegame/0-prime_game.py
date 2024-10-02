#!/usr/bin/python3
"""Module for Prime Game"""

def isWinner(x, nums):
    if x <= 0 or not nums:
        return None

    # Helper function to calculate all primes up to the max number in nums
    def sieve_of_eratosthenes(limit):
        sieve = [True] * (limit + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(limit ** 0.5) + 1):
            if sieve[i]:
                for j in range(i * i, limit + 1, i):
                    sieve[j] = False
        primes = [i for i in range(2, limit + 1) if sieve[i]]
        return primes

    # Find the maximum value of n in nums to limit our sieve
    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    # Function to count the number of primes <= n
    def count_prime_turns(n):
        count = 0
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False

        for prime in primes:
            if prime > n:
                break
            if sieve[prime]:
                count += 1
                # Remove prime and its multiples
                for multiple in range(prime, n + 1, prime):
                    sieve[multiple] = False
        return count

    # Tracking wins
    maria_wins = 0
    ben_wins = 0

    # Simulate each round
    for n in nums:
        prime_turns = count_prime_turns(n)
        if prime_turns % 2 == 1:
            maria_wins += 1  # Maria wins if the number of turns is odd
        else:
            ben_wins += 1  # Ben wins if the number of turns is even

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

