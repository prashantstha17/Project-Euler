"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
import time

def main():
    def palindromic(n):
        n = int('1'.zfill(n)[::-1]) # padding to n and reversing it to make n digit
        palindromes = {}
        for i in range(n, n*10):
            for j in range(n, n*10):
                if str(i*j) == str(i*j)[::-1]:
                    palindromes[str(i) + 'x' + str(j)] = i*j
        return palindromes
    palin = palindromic(3)
    max_palin_product = max(list(palin.values()))
    print(max_palin_product)
            
if __name__ == "__main__":
    st = time.time()
    main()
    et = time.time()
    print('Execution time:', float("{:.8f}".format(float(et - st))),'seconds')