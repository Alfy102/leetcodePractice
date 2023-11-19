




target = 23
searchArray = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
low = 0
high = len(searchArray)
index = None

while low < high:
    mid = high // 2
    if searchArray[mid] == target:
        index = mid
        break
    elif searchArray[mid] < target:
        low = mid + 1
    else:
        high = mid - 1

print(index)