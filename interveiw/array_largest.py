
def largest(numbers):
    max_val = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] > max_val:
            max_val = numbers[i]
    return max_val


nums = [10, 3, 4, 11]
result = largest(nums)
print(result)


def smallest(numbers):
    min = numbers[0]
    for i in range(1,len(numbers)):
        if numbers[i]<min:
            min=numbers[i]
    return min
            
result1 = smallest(nums)
print(result1)