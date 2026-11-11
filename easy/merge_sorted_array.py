def merge(nums1, m, nums2, n):
    """
    Let's use the two pointer method to solve this
    When merging, since it is a sorted list, the highest number will be at the end of each nums
    We can start the pointers at the back and work our way to 0 index since we need to account for cases where one nums has all the highest numbers and runs out first. In that case, we need to add the rest of the remaining nums' elements to nums1
    So each pointer start at the end of each nums
    We need to keep track of a current index so that we can know where to insert in nums1
    Run the loop while both pointers are not zero (no nums list has run out)
        In each iteration, compare the nums1[l] to nums2[r], if the former is larger or equal to,
            Replace the current index of nums1 to nums1[l]
            Decrease left pointer by 1
        Else:
            Replace the current index of nums1 to nums2[r]
            Decrease right pointer by 1
        Decrease current index by 1
    If one of the nums run out of items, we need to append the remaining nums' elements to nums1
    While the left pointer is greater than or equal to zero (if nums1 did not run out yet):
        append each element of nums1 to the current index
        Decrease left pointer by 1
        Decrease current index by 1
    While the right pointer is greater than or equal to zero (if nums2 did not run out yet):
        append each element of nums2 to the current index
        Decrease right pointer by 1
        Decrease current index by 1
    This way, we can exhaust both nums lists safely even for cases where there are no valid nums in nums1 or nums 2
    """
    l = m - 1
    r = n - 1
    current_index = (m + n) - 1
    while l >= 0 and r >= 0:
        if nums1[l] >= nums2[r]:
            nums1[current_index] = nums1[l]
            l -= 1
        elif nums2[r] > nums1[l]:
            nums1[current_index] = nums2[r]
            r -= 1
        current_index -= 1
    while l >= 0:
        nums1[current_index] = nums1[l]
        l -= 1
        current_index -= 1
    while r >= 0:
        nums1[current_index] = nums2[r]
        r -= 1
        current_index -= 1


def main():
    print(merge([2, 5, 6, 0, 0, 0], 3, [1, 7, 9], 3))


if __name__ == "__main__":
    main()
