import fibo

class Prime1k:
    def iter(self):
        total = 0
        count = 0
        i = 2

        while count < 1000:
            if fibo.isPrime(i):     # isPrime is written in fibo.py, returns true if i is prime.
                print(count, ' ', i, '\n')
                total += i
                count += 1
            i += 1
        print('sum of first 1000 prime numbers: ', total)

    # Can just change fibo.isPrime(i) to self.isPrime(i) and use below code.
    # def isPrime(self,n):  # return if number is prime or not
    #     for i in range(2, n):
    #         if n % i == 0:
    #             return False
    #     return True

Prime1k().iter()