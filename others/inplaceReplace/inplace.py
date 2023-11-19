def removeElement(nums, val: int) -> int:
    index = 0
    for number in nums:
        if number != val:
            nums[index] = number
            index += 1
    return index


input = [3,2,2,3]
val = 3
print(removeElement(input, val))