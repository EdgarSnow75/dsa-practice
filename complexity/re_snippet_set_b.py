def main():
    # B1
    def count_distinct(items):
        distinct = []
        for x in items:
            if x not in distinct:
                distinct.append(x)
        return len(distinct)

    # Time: T(n[outer loop] x n[if x not in]) = T(n^2) = O(n^2). The if x not in call gradually increases after each append and checking for an item in a collection is n so combined with outer loop n, it would be O(n^2)
    # Space: O(n) since the items in distinct grows with the input size

    # B2
    def count_distinct_fast(items):
        return len(set(items))

    # Time: T(1[len] + n[set(items)]) = O(n) since set(iteratable) is n and len(iteratable) is 1 since the list/collection knows how many items it holds
    # Space: O(n) since the produced set can grow with the input size even though we did not save it as a variable

    # B3
    def unique_sorted(items):
        return sorted(set(items))

    # Time: T(n log n[sorted()] + n[set(items)]) = T(2n log n) = O(n log n)
    # Space: O(n) since the produced set can grow with the input size even though we did not save it as a variable

    # B4
    def squares(n):
        return [i * i for i in range(n)]

    # Time: T(n[list comp with one loop]) = O(n).
    # Space: O(n) since the produced set can grow with the input size even though we did not save it as a variable

    # B5
    def empty_from_front(items):
        while items:
            items.pop(0)

    # Time: T(n[while loop] x n[items.pop(0)]) = O(n ^ 2) since for each iteration of the while loop, the first item of the collection is popped and all other items have to shift forward by one place so it is n x n which is n ^ 2
    # Space: O(1) Memory does not grow with space

    # B6
    def common(a, b):
        result = []
        for x in a:
            if x in b:
                result.append(x)
        return result

    # b as a list
    # Time: T(n[outer loop] x n[for lookup in a list]) = O(n ^ 2). It is n x n as a nested loop. The inner loop results in n since it is a lookup of a value in a list.
    # Space: O(n) the items in result grows with the input size

    # b as a set
    # Time: T(n[outer loop] x 1[for lookup in a set]) = O(n). It is n x 1 as a nested loop. The inner loop results in 1 since it is a lookup of a value in a set which is hashed.
    # Space: O(n) the items in result grows with the input size


if __name__ == "__main__":
    main()
