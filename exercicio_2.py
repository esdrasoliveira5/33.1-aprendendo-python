def arithmeticMedian(array):
    total = 0
    for number in array:
        total += number

    return total / len(array)


print(arithmeticMedian([2, 12, 23, 56, 200]))
