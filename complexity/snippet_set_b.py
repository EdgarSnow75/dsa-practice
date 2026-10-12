def main():
    # B1
    def count_distinct(items):
        distinct = []
        for x in items:
            if x not in distinct:
                distinct.append(x)
        return len(distinct)

    """
    Time: for x in items loop is O(n) and for each iteration of x, we perform a
    lookup by checking if x not in distinct which should also be O(n). In the worst case scenario
    with a lot of distinct items already in the distinct list, the inner O(n) lookup is also significant. 
    It's O(n^2)
    
    Space: O(n) since the number of distinct items grow with the size of n which means memory
    used grows with input
    """

    # B2
    def count_distinct_fast(items):
        return len(set(items))

    """
    Time: O(n) the steps it takes to create a set is proportional to the size of the input
    Space: O(n) since the memory size of the set is proportional to the size of the input
    """

    # B3
    def unique_sorted(items):
        return sorted(set(items))

    """
    Time:  O(n log n) since set(items) is O(n) amd sorted is O(n log n). They are in sequence.
    Space: O(n) the returned output increases with the input size 
    """

    # B4
    def squares(n):
        return [i * i for i in range(n)]

    """
    Time: O(n) since it is a for i in range loop
    Space:  O(n) since the memory size increases with the input size of n
    """

    # B5
    def empty_from_front(items):
        while items:
            items.pop(0)

    """
    Time: O(n ^ 2). items.pop(0) is O(n) because for each look up, we remove the first item of the list and shift the items which should also be O(n)
    Space: O(1) since we only create a popped item temporary without even storing it
    """

    # B6
    def common(a, b):
        result = []
        for x in a:
            if x in b:
                result.append(x)
        return result

    # a
    """
    Time: O(n ^ 2). x in b lookup in a list O(n) is nested inside the outer x in a loop O(n).
    Space: O(n) the size of result grows with the input size n
    """
    # b
    """
    Time: O(n). An inner x in b lookup in a set is O(1) which is nested inside the O(n) x in a loop
    Space: O(n) the size of result grows with the input size n
    """


if __name__ == "__main__":
    main()
