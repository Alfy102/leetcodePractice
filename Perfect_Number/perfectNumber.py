def perfectNumber(input: int) -> int:
    sum = 0
    listOfNumber = []
    for i in range(1, input):
        if input%i == 0:
            listOfNumber.append(i)
            sum += i
    print(listOfNumber)
    return sum

input = 6
print(perfectNumber(input= input))