def find_smallest(numbers):
    if len(numbers) == 0:
        return None

    largest = numbers[0]
    
    for number in numbers:
        if number < largest:
            largest = number 
    return largest
print(find_smallest([8, 3, 12, 1, 7]))
print(find_smallest([-3, -10, -1, -6]))
print(find_smallest([]))