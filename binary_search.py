# Challenge: Find the target within the list of prime numbers

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def binary_search(prime_list, target):
# find the min and max indices
    min = 0
    max = len(prime_list) - 1
    guess_index = 0

    # Means that target is not present within the array; return a number that is not within the bound of the array
    # (any negative num will work)
    if max < min:
        return -1

    while min < max:

        # find the average index to get to the middle index; use integer division to get whole int, not decimal
        guess_index = (min + max) // 2

        # if guess index = target index, we've found the target
        if primes[guess_index] == target:
            return guess_index

        # if guess index is larger than target, then the target is in the left half of the list
        # shift max or ceiling to equal guess_index - 1
        if primes[guess_index] > target:
            max = guess_index - 1
        # otherwise, if guess_index is less than target, then the target is in the right half of the list; shift guess_index
        else:
            min = guess_index + 1

    return guess_index

if __name__ == '__main__':
    result = binary_search(primes, 67)
    print(result)

