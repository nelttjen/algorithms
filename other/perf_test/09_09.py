# Place the following functions below in order of their efficiency.
# They all take in a list of numbers between 0 and 1.
# The list can be quite long. An example input list would be [random.random () for i in range (100000)].
# How would you prove that your answer is correct? - profiling?
import random
import time

def timeit(func):
    def timed(*args, **kw):
        ts = time.perf_counter()
        result = func(*args, **kw)
        te = time.perf_counter()
        print('%r  %2.2f s' % (func.__name__, te - ts))
    return timed

@timeit
def f1 (lIn):
            l1 = sorted (lIn)
            l2 = [i for i in l1 if i <0.5]
            return [i * i for i in l2]
@timeit
def f2 (lIn):
            l1 = [i for i in lIn if i <0.5]
            l2 = sorted (l1)
            return [i * i for i in l2]
@timeit
def f3 (lIn):
            l1 = [i * i for i in lIn]
            l2 = sorted (l1)
            return [i for i in l1 if i <(0.5 * 0.5)]


if __name__ == '__main__':
    arr = [random.random () for i in range (10000000)]
    f1(arr)
    f2(arr)
    f3(arr)