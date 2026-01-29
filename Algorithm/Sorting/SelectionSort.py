# Time Complexity: O(n^2) - We always scan the remaining unsorted list.
# Memory Complexity: O(1) - Performs the sort in-place.

def selectionSort(nums: list[int]) -> list[int]:
    n = len(nums)
    print(f"Starting Selection Sort on: {nums}\n" + "-" * 50)

    # The outer loop moves the boundary between the sorted and unsorted parts.
    for i in range(n):
        # 1. Assume the first element of the unsorted part is the minimum.
        min_index_ptr = i
        print(f"Iteration {i + 1}: Assuming index {i} (value: {nums[i]}) is the minimum.")

        # 2. INNER LOOP (The Search):
        # Check every other element in the unsorted part to find the TRUE minimum.
        for j in range(i + 1, n):
            print(f"  Comparing {nums[min_index_ptr]} with {nums[j]}...", end="")

            if nums[j] < nums[min_index_ptr]:
                print(f" Found new minimum! index {j} (value: {nums[j]})")
                min_index_ptr = j
            else:
                print(" No change.")

        # 3. THE SWAP:
        # Swap the smallest element found with the first element of the unsorted part.
        nums[i], nums[min_index_ptr] = nums[min_index_ptr], nums[i]
        print(f"  Swapped: {nums}\n")

    return nums


nums = [2, 6, 2, 5, 1]
sorted_nums = selectionSort(nums)
print(f"Final sorted number: {sorted_nums}")