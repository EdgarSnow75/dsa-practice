# LeetCode 509
import time as tm


# Recursive
def re_fib(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return re_fib(n - 1) + re_fib(n - 2)


# Loop
def loop_fib(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    total_sum = 0
    n_prev1 = 0
    n_prev2 = 1
    for _ in range(2, n + 1):
        total_sum = n_prev1 + n_prev2
        n_prev1 = n_prev2
        n_prev2 = total_sum
    return total_sum


def main():
    print("Time for Recursive Fib")
    start_time = tm.perf_counter()
    print(re_fib(30))
    end_time = tm.perf_counter()
    print(f"Time taken: {end_time - start_time}s")
    print(start_time)
    print(end_time)
    print("---------------------------------------")
    print("Time for Loop Fib")
    start_time = tm.perf_counter()
    print(loop_fib(30))
    end_time = tm.perf_counter()
    print(f"Time taken: {end_time - start_time}s")
    print(start_time)
    print(end_time)


"""
Time for Recursive Fib
6765
Time taken: 0.0018108999993273756s
7911.4590261
7911.460837
---------------------------------------
Time for Loop Fib
6765
Time taken: 3.3600000278966036e-05s
7911.4610574
7911.461091

For times to be this apart, we can say that this is mainly because in the recursive version, each one run of the function is essentially O(1) (T(1 + 1 + 1(maybe 2 if we count both function calls)))
and for the loop version, we now depend on the input size because the loop goes on longer if the input size is large, so it is O(n).
"""

if __name__ == "__main__":
    main()
