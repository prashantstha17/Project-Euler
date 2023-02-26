"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import time

def main():
    def generate_prime(n):
        primes = []
        a = 2
        while 2 <= n:
            if n % a == 0:
                n = n / a
                primes.append(a)
            else:
                a = a + 1
        return primes
    print(max(generate_prime(600851475143)))

if __name__ == "__main__":
    st = time.time()
    main()
    et = time.time()
    print('Execution time:', float("{:.8f}".format(float(et - st))),'seconds')