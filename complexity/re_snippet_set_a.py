def main():
    # A1
    def first_item(items):
        return items[0]

    # Time: O(1[fetch the item at index] + 1[return the item]) simplified to O(1) since I can only see the index lookup of an item and it is a singular step
    # Space: O(1) No notable memory used

    # A2
    def total(items):
        result = 0
        for x in items:
            result += x
        return result

    # Time: T(n[loop] + n[increment inside loop] + 1[return the results]) = T(2n + 1) to O(n). It uses a loop that go throughs all the items in the collection so this step grows with the input size
    # Space: O(1) since while the value of result may increase, it still is a single variable

    # A3
    def print_twice(items):
        for x in items:
            print(x)
        for x in items:
            print(x, x)

    # Time: T(n[loop] + n[print] + n[loop] + n[print]) = T(4n) = O(n). Two loops not nested.
    # Space: O(1) Memory does not grow with input.

    # A4
    def has_pair_with_sum(items, target):
        for i in range(len(items)):
            for j in range(i + 1, len(items)):
                if items[i] + items[j] == target:
                    return True
        return False

    # Time: T(n[Outer loop] x n[inner loop] + 1[conditional check] + 1[return boolean] + 1[return boolean]) = T(n^2 + 3) = O(n^2). Nested loop.
    # Space: O(1). Memory does not grow with input.

    # A5
    def halvings(n):
        steps = 0
        while n > 1:
            n = n // 2
            steps += 1
        return steps

    # Time: T(n[loop] + log n[Halving of the input] + 1[Increment steps] + 1[return steps]) = T(n + log n + 1) = O(log n) because the steps halves by 2 for each iteration
    # Space: O(1). Memory does not grow with input.

    # A6
    def print_grid(rows, cols):
        for r in range(rows):
            for c in range(cols):
                print(r, c)

    # Time: T(r[Outer loop] x c[inner loop] + 1[print]) = T(r x c + 1) = O(r x c). Because they are different collections used in the outer loop and in the inner loop
    # Space: O(1). Memory does not grow with input.

    # A7
    def count_steps(items):
        count = 0
        for x in items:
            for k in range(5):
                count += 1
        return count

    # Time: T(n[outer loop] x 5 [Inner loop of 5] + 1[increment count] + 1[return count]) = T(5n + 2) = O(n). Even though this is a nested loop, the inner loop is a constant which means the steps only grows once with the input size and not in powers.
    # Space: O(1). Memory does not grow with input.


if __name__ == "__main__":
    main()
