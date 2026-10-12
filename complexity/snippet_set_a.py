def main():
    # A1
    def first_item(items):
        return items[0]

    # O(1) because it is an index lookup which does not grow with the input size
    # Space complexity is O(1) as well since looking up the number and returning it only takes minimal/single space

    # A2
    def total(items):
        result = 0
        for x in items:
            result += x
        return result

    # Time: O(n) since we are going through all the items in the input list and summing up the value
    # Space: O(1) we only ever a few variables like results and x to store values so it should not be heavy on memory

    # A3
    def print_twice(items):
        for x in items:
            print(x)
        for x in items:
            print(x, x)

    # Time: O(2n) since its two loops but will be regularized to O(n) according to Big-O rules
    # Space: O(1) since we are only ever using minimal space for the single variable x and we do not store anything

    # A4
    def has_pair_with_sum(items, target):
        for i in range(len(items)):
            for j in range(i + 1, len(items)):
                if items[i] + items[j] == target:
                    return True
        return False

    """
    Let's do the pair counting. If n = 4, the pairs would be (1 x 3) + (1 x 2) + 1 = 6 and for n = 1,000
    since the basic formula for combination is n(n-1)/2, it would be 1000 x 999 / 2 which is 499500.
    Since it is a nested loop and the inner loop will run the full list of items for a decent number of times, we should give it a O(n^2)
    but I do not know how to account for the number of inner loop runs causing less than the ones before it
    Time is O(n^2)
    For space, I think its O(1) because we are only creating the loop counters
    """

    # A5
    def halvings(n):
        steps = 0
        while n > 1:
            n = n // 2
            steps += 1
        return steps

    # Time: O(log n) since the value of n is halved in each step and the number of step it takes to reach 1
    # is the logarithmic base 2 of n
    # Space is small, O(1) since we are only using steps and n

    # A6
    def print_grid(rows, cols):
        for r in range(rows):
            for c in range(cols):
                print(r, c)

    # Time  O(r x c) since we run the whole c for every r
    # Space: O(1) since we are not storing anything

    # A7
    def count_steps(items):
        count = 0
        for x in items:
            for k in range(5):
                count += 1
        return count

    # Time:  O(n) even though it has a nested loop, the nested loop does not grow with the input size and has a fixed 5 so n x 5 should just be n
    # Space:  O(1) since we only use x, k and count. Nothing is appended or nor the variable sizes enlarged


if __name__ == "__main__":
    main()
