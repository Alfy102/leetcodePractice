def isPalindrome(x: int) -> bool:
    stringNum = str(x)
    reversedStringNum = stringNum[::-1]
    return stringNum == reversedStringNum

input = 1234321
print(isPalindrome(input))