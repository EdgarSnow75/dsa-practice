import time

from tabulate import tabulate

data = {}


def find_item(n, target):
    for num in n:
        if num == target:
            return True


def timing_check(n, target):

    start_time = time.perf_counter()
    find_item(n, target)
    end_time = time.perf_counter()
    return f"{n} took {end_time - start_time:.4f} seconds"


def run_timing_check(n, target, counts):
    total_duration = 0.0
    iterations = counts
    while iterations > 0:
        start_time = time.perf_counter()
        find_item(n, target)
        end_time = time.perf_counter()
        total_duration += end_time - start_time
        iterations -= 1
    average_duration = total_duration / counts if counts > 0 else 0.0
    data.setdefault(len(n), {})[type(n).__name__] = f"{average_duration:.4f} seconds"


def print_all():
    rows = [[n, t["list"], t["set"]] for n, t in data.items()]
    print(
        tabulate(
            rows, headers=["Length", "List Duration", "Set Duration"], tablefmt="github"
        )
    )


run_timing_check(list(range(1000)), -1, 16)  # Time should be very clost to 0 seconds
run_timing_check(
    list(range(10000)), -1, 16
)  # I think the list time should grow ten times than the last.
run_timing_check(
    list(range(100000)), -1, 16
)  # I think the list time should grow ten times than the last.
run_timing_check(
    list(range(1000000)), -1, 16
)  # I think the list time should grow ten times than the last.
run_timing_check(
    list(range(10000000)), -1, 16
)  # I think the list time should grow ten times than the last.


run_timing_check(
    set(range(1000)), -1, 16
)  # Time should be very clost to 0 seconds. I think set times might be faster than list
run_timing_check(
    set(range(10000)), -1, 16
)  # I think the list time should grow ten times than the last.
run_timing_check(
    set(range(100000)), -1, 16
)  # I think the list time should grow ten times than the last.
run_timing_check(
    set(range(1000000)), -1, 16
)  # I think the list time should grow ten times than the last.
run_timing_check(
    set(range(10000000)), -1, 16
)  # I think the list time should grow ten times than the last.

print_all()

"""
Note about the results
--------------------------
I did not expect sets to take more than lists for iterations but it should make sense since there are no duplicate items that sets could get an advantage over lists.
The seconds were much smaller than I expected; all well under 300 miliseconds
The difference in each length jump was ten times as expected except for the first length jump to the second
"""
