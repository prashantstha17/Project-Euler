"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
import time

def main():
    def smallest_divisible(n):
        # Initialize a list to store the prime factors and their powers
        factors = []
        # Loop through all numbers from 2 to n and factorize each number
        for i in range(2, n+1):
            # Loop through all prime factors of i and update their powers in the factors list
            for j in range(0, len(factors)):
                if i % factors[j][0] == 0:
                    count = 0
                    while i % factors[j][0] == 0:
                        i //= factors[j][0]
                        count += 1
                    factors[j][1] = max(factors[j][1], count)
            # If i has a new prime factor, add it to the factors list
            if i > 1:
                factors.append([i, 1])
        # Calculate the smallest positive number that is evenly divisible by all of the numbers from 1 to n
        # print(factors)
        result = 1
        for factor in factors:
            result *= factor[0]**factor[1]
        return result

    print(smallest_divisible(20))

if __name__ == "__main__":
    st = time.time()
    main()
    et = time.time()
    print('Execution time:', float("{:.8f}".format(float(et - st))),'seconds')



# Explaination
"""
Sure, to find the smallest positive number that is evenly divisible by all of the numbers from 1 to 10, we can use a similar approach as we did for finding the smallest positive number that is evenly divisible by all of the numbers from 1 to 20. Here are the steps:

List out the prime factors of each number from 1 to 10:
1: 1
2: 2
3: 3
4: 2^2
5: 5
6: 2 * 3
7: 7
8: 2^3
9: 3^2
10: 2 * 5
For each prime factor, determine the maximum number of times it appears in the prime factorization of any of the numbers from 1 to 10:
2 appears a maximum of 3 times (in the prime factorization of 8)
3 appears a maximum of 2 times (in the prime factorization of 9)
5 appears a maximum of 1 time (in the prime factorization of 5)
7 appears a maximum of 1 time (in the prime factorization of 7)
Multiply together the prime factors raised to their maximum powers:
2^3 * 3^2 * 5 * 7 = 2520.

Therefore, the smallest positive number that is evenly divisible by all of the numbers from 1 to 10 is 2520.
"""