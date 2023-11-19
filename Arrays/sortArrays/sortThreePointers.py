def sortColors(nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    low, mid, high = 0, 0, len(nums)-1
    while mid <= high:
        print('=======================')
        print(nums)
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
        print('=======================')
        print(nums)
        print(low)
        print(mid)
        print(high)

    
sortColors([2,0,2,1,1,0, 1,2,0])