def reverse_list(numbers):
    reversed_numbers = []
    for index in range(len(numbers) -1, -1, -1):
        reversed_numbers.append(numbers[index])
    return reversed_numbers 
print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list([10, 20, 30]))
print(reverse_list([]))