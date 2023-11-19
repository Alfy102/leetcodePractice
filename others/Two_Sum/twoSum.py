def twoSum(nums, target):
    numberMap= dict(enumerate(nums))
    possibleIndex = []
    for i in range(len(nums)):
        remain = target - nums[i]
        if remain in numberMap.values():
            for index, value in numberMap.items():
                if value == remain and index != i:
                    possibleIndex.append(i)
    return possibleIndex

        

numbers = [0, 3, 2, 3, 0]
target = 0
print(twoSum(nums= numbers, target= target))