#!/usr/bin/python3
"""Module defining isWinner function."""

def is_prime(num):
    """Checks if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_winner(x, nums):
    """Determines the winner of the game."""
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes = [num for num in range(2, n + 1) if is_prime(num)]
        is_maria_turn = True

        while primes:
            if is_maria_turn:
                prime = primes[0]
                primes = [num for num in primes if num % prime != 0]
            else:
                prime = primes[-1]
                primes = [num for num in primes if num % prime != 0]
            is_maria_turn = not is_maria_turn

        if is_maria_turn:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
