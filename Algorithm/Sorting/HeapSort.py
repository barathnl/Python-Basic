def heapify(nums:list[int], n:int, i:int):
    largest = i
    left = 2*i+1 # Left child to root index 'i'
    right = 2*i+2 # Right child to root index 'i'

    # Check if left child exists and is greater than root
    if left < n and nums[left] > nums[largest]:
        largest = left

    # Check if right child exists and is greater than largest so far
    if right < n and nums[right] > nums[largest]:
        largest = right

    # If largest is not root, swap and continue heapifying
    if largest != i:
        nums[i] , nums[largest] = nums[largest] , nums[i]
        heapify(nums,n,largest)

def heap_sort(nums:list[int]) -> list[int]:
    n = len(nums)

    # 1. Build a Max-Heap
    for i in range(n//2-1,-1,-1):
        heapify(nums,n,i)

    # 2. Extract elements one by one
    for i in range(n-1,0,-1):
        nums[i] , nums [0] = nums[0] , nums[i] # Biggest number is at index 0, swap to last index
        heapify(nums,i,0) # Restore heap on the remaining elements

    return nums

nums = [2,6,2,5,1]
sorted_nums = heap_sort(nums)
print(f"Final sorted number {sorted_nums}")