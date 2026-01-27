def selectionSort(nums:list[int]) -> list[int]:
    n = len(nums)
    print(f"Starting Selection Sort on: {nums}\n" + "-" * 50)
    for i in range(n):
        min_index_ptr = i
        print(f"Iteration {i + 1}: Assuming index {i} (value: {nums[i]}) is the minimum.")
        for j in range (i+1,n):
            print(f"  Comparing {nums[min_index_ptr]} with {nums[j]}...", end="")
            if nums[j] < nums[min_index_ptr]:
                print(f" Found new minimum! index {j} (value: {nums[j]})")
                min_index_ptr = j
            nums[i] , nums[min_index_ptr] = nums[min_index_ptr] , nums [i]
    return nums

nums = [2,6,2,5,1]
sorted_nums = selectionSort(nums)
print(f"Final sorted number {sorted_nums}")

