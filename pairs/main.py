def pairs_with_given_sum (numbers, target):
    counter = 0
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                counter += 1
    return counter
print(pairs_with_given_sum ([6, 0], 6))
# print(pairs_with_given_sum ([1, 2, 4, 5], 6))
# print(pairs_with_given_sum ([97, 51, 49, 35, 3, 65], 100))