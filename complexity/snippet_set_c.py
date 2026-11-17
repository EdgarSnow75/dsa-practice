COUNT_RE = 0


# S1
def power(base, exp):
    if exp == 0:
        return 1
    half = power(base, exp // 2)
    if exp % 2 == 0:
        return half * half
    return half * half * base


# Time: O(log n) because the exp is halved by 2 each step and its only a matter of how much halvings it takes for exp to become 1 and plus 2 more steps (1 for exp = 1 and exp = 0 which is unaccounted for because they are constants)

# Space: O(log n) because the call stack is the number of calls needed for exp to be 0 which is log n + 2


# S2
def sum_list(items):
    if not items:
        return 0
    return items[0] + sum_list(items[1:])


# In this case, items should be n. Time is O(n) since the amount of elements in the items list can increase the recursion calls.
# Space: It should be O(n) since each recursion creates a new list.


# S3
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


# In this case, n is n. Time is O(2^n) because I think the number of step increases by the power of 2 whenever the input is increased
# For Space: it shoould be O(n) since the callstack is not double-stacked and we tackle n-1 first before we do n-2 calls


# S4
def count_digits(n):
    count = 1
    while n >= 10:
        n //= 10
        count += 1
    return count


# I think Time is O(log_10 n) because we half the problem by 10 times every iteration of the loop
# Space: It should be O(1)


# S5
def first_repeat(items):
    for i in range(len(items)):
        for j in range(i):
            if items[i] == items[j]:
                return items[i]
    return None


# I think the best is Omega(1) if the first and second items are the same. The nested loop will run one time regardless thou. O(n^2) because its a nested loop?
# Space: O(1)


# S6
def group_by_length(words):
    groups = {}
    for w in words:
        groups.setdefault(len(w), []).append(w)
    return groups


# I think ultimately it should be still O(n) because even though we have a look up using setdefault, it is a hashed look up and append's armotized cost is O(1) anyways
# Space is O(n) I think list grows with the inpuit
