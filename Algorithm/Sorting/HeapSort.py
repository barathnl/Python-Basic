# Time Complexity: O(n log n) - Much faster than Bubble Sort for large lists!
# Memory Complexity: O(1) - Also sorts in-place.

def heapify(nums: list[int], n: int, i: int):
    """
    Ensures the subtree rooted at index 'i' satisfies the Max-Heap property:
    The parent must be larger than its children.
    """
    largest = i
    left = 2 * i + 1  # Standard formula to find left child in an array-based tree
    right = 2 * i + 2  # Standard formula to find right child

    # If left child is within bounds and bigger than the current largest
    if left < n and nums[left] > nums[largest]:
        largest = left

    # If right child is within bounds and bigger than the current largest
    if right < n and nums[right] > nums[largest]:
        largest = right

    # If the root wasn't the largest, we need to swap and keep fixing downward
    if largest != i:
        nums[i], nums[largest] = nums[largest], nums[i]
        # Recursively heapify the affected sub-tree
        heapify(nums, n, largest)


def heap_sort(nums: list[int]) -> list[int]:
    n = len(nums)

    # 1. Build a Max-Heap: Rearrange the array into a heap structure.
    # We start from the last non-leaf node and move upwards.
    for i in range(n // 2 - 1, -1, -1):
        heapify(nums, n, i)

    # 2. Extraction: One by one, move the top of the heap (largest) to the end.
    for i in range(n - 1, 0, -1):
        # Swap the current root (max value) with the last element
        nums[i], nums[0] = nums[0], nums[i]

        # Call heapify on the reduced heap (excluding the sorted end) to find the next max
        heapify(nums, i, 0)

    return nums


# Test Data
nums = [2, 6, 2, 5, 1]
sorted_nums = heap_sort(nums)
print(f"Final sorted number: {sorted_nums}")