
def pairs_with_given_sum (numbers, target):
    if not numbers:
        return 0
    
    if not all(isinstance(num, int) for num in numbers) or not isinstance(target, int):
        raise ValueError("You can enter only numbers and the target must be an integer!")
    
    if len(numbers) == 1:
        return 0
    
    hash_table = {}
    counter = 0
    
    for num in numbers:
        complement = target - num
        
        if complement in hash_table:
            counter += 1    
        hash_table[num]= True
        
    return counter

print(pairs_with_given_sum ([3, 3, 3], 6))
# print(pairs_with_given_sum ([6, 'a', 'b'], 6))
# print(pairs_with_given_sum([-2, 1, 2, -1], 0))
# print(pairs_with_given_sum ([1, 2, 4, 5], 6))
# print(pairs_with_given_sum ([-10, -3, -7, -1], -10))
# print(pairs_with_given_sum ([97, 51, 49, 35, 3, 65], 100))