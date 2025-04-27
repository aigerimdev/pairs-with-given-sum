from pairs.main import pairs_with_given_sum
import pytest
# example input 1: [], 6
# expected output 1: 0

# example input 2: [6], 6
# expected output 2: 0

# example input 3: [6, 0, 3], 6
# expected output 3: 1

# example input 4: [-10, -3, -7, -1], -10
# expected output 4: 1

# example input 5: numbers = [3, 'b', '3'], 6
# expected output 5: ValueError ("You can enter only numbers!")

# example input 6: [-2, 1, 2, -1], 0
# expected output 6: 2

# test1
def test_if_list_is_empty():
    # arrange
    numbers = []
    target = 6
    expected = 0
    # act
    expected = pairs_with_given_sum(numbers, target)
    # assert
    assert expected == expected

# test2
def test_gives_number_of_pairs():
    # arrange
    numbers = [1, 2, 4, 5]
    target = 6
    expected = 2
    # act
    expected = pairs_with_given_sum(numbers, target)
    # assert
    assert expected == expected

# test3
def test_if_list_has_only_one_number_and_that_number_equal_to_target():
    # arrange
    numbers = [6]
    target = 6
    expected = 0
    # act
    expected = pairs_with_given_sum(numbers, target)
    # assert
    assert expected == expected

# test4
def test_if_number_equal_to_zero():
    # arrange
    numbers = [6, 0, 3]
    target = 6
    expected = 1
    # act
    expected = pairs_with_given_sum(numbers, target)
    # assert
    assert expected == expected
        
# test6
def test_if_the_target_not_integer():
    # arrange
    numbers = [3, 4, 5]
    target = "a"
    # act and assert
    with pytest.raises(ValueError):
        pairs_with_given_sum(numbers, target)
# test5
def test_if_the_input_of_numbers_is_none_integer():
    # arrange
    numbers = [3, 'b', '3']
    target = 6
    # act and assert
    with pytest.raises(ValueError):
        pairs_with_given_sum(numbers, target)
# test7
def test_if_the_target_is_negative_number():
    # arrange
    numbers = [-10, -3, -7, -1]
    target = -10
    expected = 1 #-3+(-7)= -10
    # act
    expected = pairs_with_given_sum(numbers, target)
    # assert
    assert expected == expected
    
# test8
def test_if_the_target_is_zero():
    # arrange
    numbers = [-2, 1, 2, -1]
    target = 0
    expected = 2 #-2+2=0, 1+(-1)=0
    # act
    expected = pairs_with_given_sum(numbers, target)
    # assert
    assert expected == expected
    


