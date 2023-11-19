def moveZeroes(nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    low = 0
    for index in range(len(nums)):
        if nums[index] != 0 and nums[low] == 0:
            nums[low], nums[index] = nums[index], nums[low]
        if nums[low] != 0:
            low += 1


moveZeroes([0])