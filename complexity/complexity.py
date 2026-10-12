def complexity():
    items = [1, 2, 3, 4, 5]
    # O(1) is a time complexity where the program only takes one step to run regardless of the input size
    items[1]
    # Lookups like these at the precise index position is O(1) because we only access one element

    # O(log n) is a time complexity where the program throws away half of the remaining items before when running
    # Examples include binary search
    def binary_search(current_items, low, high, target_item):
        if high >= low:
            mid = low + (high - low) // 2

            if current_items[mid] == target_item:
                return mid
            elif current_items[mid] > target_item:
                return binary_search(current_items, low, mid - 1, target_item)
            else:
                return binary_search(current_items, mid + 1, high, target_item)
        else:
            return -1

    # O(n) means the step grows with the input
    # Examples include linear search and ordinary lookups
    key_item = 3
    for item in items:
        if key_item == item:
            return True

    # O(n^2) means the step grows exponentially with the input size
    for i in range(len(items)):
        for j in range(1, len(items)):
            if items[i] < items[j]:
                temp = items[i]
                items[i] = items[j]
                items[j] = temp
