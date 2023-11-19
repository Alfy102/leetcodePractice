from collections import Counter
# sliding window

def checkInclusion(string1: str, string2: str) -> bool:
    # get hash map of all char counts
    countMap = Counter(string1)
    windowSize = len(string1)
    matched = 0

    for index in range(len(string2)):
        print('============================')
        if string2[index] in countMap: 
            countMap[string2[index]] -= 1
            if countMap[string2[index]] == 0:
                matched += 1
        print(countMap)
        print(matched)
        if index >= windowSize and string2[index-windowSize] in countMap: 
            if countMap[string2[index-windowSize]] == 0:
                matched -= 1
            countMap[string2[index-windowSize]] += 1
        print('============================')
        if matched == len(countMap):
            return True
    return False


print(checkInclusion("dbb", "eidbbaooo"))