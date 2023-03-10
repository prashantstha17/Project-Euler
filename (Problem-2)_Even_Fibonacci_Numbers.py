"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
find the sum of the even-valued terms.
"""
import time

def main():
    def fib(n):
        lis = []
        num1 = 0
        num2 = 1
        while num1 < n:
            lis.append(num1)
            num1, num2 = num2, num1+num2
        return lis
    fib_values = fib(4000000)
    fib_even_values = [even for even in fib_values if (even%2 == 0)]
    print(sum(fib_even_values))


if __name__ == "__main__":
    st = time.time()
    main()
    et = time.time()
    print('Execution time:', float("{:.8f}".format(float(et - st))),'seconds')