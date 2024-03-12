import random
import math

def fisher_yates_shuffle(n):
    """ Generate a random permutation of 0 to n-1. """
    arr = list(range(n))
    for i in range(n-1, 0, -1):
        j = random.randint(0, i)
        arr[i], arr[j] = arr[j], arr[i]
    return arr

def count_fixed_points(permutation):
    """ Count the number of fixed points in a permutation. """
    return sum(1 for i in range(len(permutation)) if permutation[i] == i)

def average_fixed_points_experimental(n, num_trials=1000):
    """ Calculate the experimental average number of fixed points for permutations of [n]. """
    total_fixed_points = sum(count_fixed_points(fisher_yates_shuffle(n)) for _ in range(num_trials))
    return total_fixed_points / num_trials


# Calculate and display results
for n in range(1, 101):
    avg_experimental = average_fixed_points_experimental(n)
    print(f"n = {n}: Experimental average = {avg_experimental}")
