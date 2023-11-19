def reverseWords(self, s: str) -> str:
    stringList = s.split(' ')
    for index, word in enumerate(stringList):
        stringList[index] = word[::-1]
    return ' '.join(stringList)