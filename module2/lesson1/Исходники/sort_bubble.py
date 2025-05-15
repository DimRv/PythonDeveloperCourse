def bubble_sorting(numbers):
    flag = True
    while flag:
        flag = False
        for i in range(len(numbers) - 1):
            if numbers[i] > numbers[i + 1]:
                numbers[i],numbers[i + 1] = numbers[i + 1],numbers[i]
                flag = True
    return numbers

print(bubble_sorting([7,5,2,9]))