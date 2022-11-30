import random
import time
import cppyy
import math
cppyy.cppdef('''
#include <cmath>


unsigned long long factorization(unsigned long long int n){
    if (n % 2 == 0)
        return 2;
    for (int i = 3; i < sqrt(n); i +=2){
        if (n % i == 0)
            return i;
    }
  return 0;
}
''')


def factorization_py(n):
    if (n % 2 == 0):
        return 2
    for i in range(3, math.isqrt(n), 2):
        if n % i == 0:
            return i
    return 0



from cppyy.gbl import factorization


def main():
    factorization(10)# первый тест и очень большие затраты времяни на компилцию
    l = 20000503 - 2
    col_test = 10
    t1 = time.time()
    for i in range(l, l + col_test):
        factorization_py(i)
    print(time.time() - t1)
    t1 = time.time()
    for i in range(l, l + col_test):
        factorization(i)
    print(time.time() - t1)

if __name__ == "__main__":
    main()