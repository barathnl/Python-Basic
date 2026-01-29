# Time complexity : O(n^2) - Due to nested loops (comparing every pair)
# Memory complexity : O(1) - "In-place" sort; no extra lists are created
def bubbleSort(nums: list[int]) -> list[int]:
    n = len(nums)

    # Outer loop: Controls how many times we pass through the list.
    # After each pass, the largest remaining element is "bubbled" to its correct position.
    for i in range(n):

        # Inner loop: Compares adjacent elements.
        # We use (n - i - 1) because the last 'i' elements are already sorted.
        for j in range(0, n - i - 1, 1):

            # If the current element is bigger than the next, swap them.
            if nums[j] > nums[j + 1]:
                # Pythonic swap: No need for a temporary 'temp' variable!
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums


# Driver code to test the function
nums = [2, 6, 2, 5, 1]
sortedNums = bubbleSort(nums)
print(f"Final sorted number: {sorted_nums}") # Expected Output: [1, 2, 2, 5, 6]