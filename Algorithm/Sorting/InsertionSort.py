# Time Complexity: O(n^2) - Average/Worst case (nested loops)
# Time Complexity: O(n) - Best case (if the list is already sorted)
# Memory Complexity: O(1) - In-place sorting

def insertionSort(nums: list[int]) -> list[int]:
    n = len(nums)

    # We start from index 1 because the first element (index 0) is considered "sorted" by itself.
    for i in range(1, n):
        key = nums[i]  # The "card" we are currently picking up to insert
        j = i - 1  # The index of the element just to the left of our key

        print(f"Checking element {key} in {nums}")

        # Move elements of nums[0..i-1] that are greater than the key
        # to one position ahead of their current position.
        # This creates the "gap" where the key will eventually land.
        while j >= 0 and key < nums[j]:
            nums[j + 1] = nums[j]  # Shift the larger element to the right
            print(f"  Shifting {nums[j]} to the right: {nums}")
            j -= 1

        # Once we find the correct spot (or hit the start of the list),
        # we drop the 'key' into its sorted position.
        nums[j + 1] = key
        print(f"  Inserting {key}: {nums}\n")

    return nums


nums = [2, 6, 2, 5, 1]
sorted_nums = insertionSort(nums)
print(f"Final sorted number {sorted_nums}")