"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
"""
import time
def main():
    def generate_primes(n):
        primes = []
        num = 2
        while len(primes) < n:
            # check if num is prime
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                primes.append(num)
            num+=1
        return primes[-1]
    print(generate_primes(10001))

if __name__ == "__main__":
    st = time.time()
    main()
    et = time.time()
    print('Execution time:', float("{:.8f}".format(float(et - st))),'seconds')

