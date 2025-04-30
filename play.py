def pairs_with_given_sum (numbers, target):
    hash_table = {}
    counter = 0
    
    for num in numbers:
        complement = target - num
        
        if complement in hash_table:
            counter += 1
            
        hash_table[num]= True
    return counter
            
    
print(pairs_with_given_sum ([1, 2, 1, 4, 5], 6))


def pairs_with_given_sum (numbers, target):
    if numbers == []:
        return 0
    if not all (isinstance(num, int) for num in numbers):
        raise ValueError ("You can enter only numbers!")
    counter = 0
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                counter += 1
    return counter
print(pairs_with_given_sum ([6, 0], -6))


# option 3
def pairs_with_given_sum(numbers, target):
    count = 0
    freq = {}
    
    for number in numbers:  #
        complement = target - number
        if complement in freq:
            count += freq[complement]
        
        freq[number] = freq.get(number, 0) + 1

    return count

print(pairs_with_given_sum ([1, 4, 4, 1], 5))
        