
numbers = [8, 6, 7, 4, 5, 2, 3, 1]

unsorted = True

while(unsorted):
    unsorted = False
    for i in range(1, len(numbers)):
        if numbers[i] < numbers[i - 1]:  # (i-1),i
            unsorted = True              # numbers = [8, 6, 7, 4, 5, 2, 3, 1]
            tmp = numbers[i]
            numbers[i] = numbers[i - 1]  # numbers = [8, 8, 7, 4, 5, 2, 3, 1]
            numbers[i - 1] = tmp  # numbers = [8, 8, 7, 4, 5, 2, 3, 1]

print(numbers)
