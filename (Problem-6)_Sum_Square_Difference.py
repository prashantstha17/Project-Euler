"""
The sum of the squares of the first ten natural numbers is,
    1**2 + 2**2 + .... + 10**2 = 385

The square of the sum of the first ten natural numbers is,
    (1+2+....+10)**2 = 55*2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 
    3025 - 385 = 2640
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
import time
def main():
    def find_diff(n):
        squres_sum =  sum([x**2 for x in range(1, n+1)])
        sum_sqaures = sum([x for x in range(1, n+1)])**2
        return sum_sqaures - squres_sum
    print(find_diff(100))

if __name__ == "__main__":
    st = time.time()
    main()
    et = time.time()
    print('Execution time:', float("{:.8f}".format(float(et - st))),'seconds')
