def romanToInt(s: str) -> int:
    romanMap = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }
    sum = 0
    for i, char in enumerate(s):
        if i < len(s)-1 and romanMap[char] < romanMap[s[i + 1]]:
            sum -= romanMap[char] 
        else:
            sum += romanMap[char]

    return sum

input = 'VI'
print(romanToInt(input))