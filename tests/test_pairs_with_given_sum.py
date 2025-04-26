from pairs.main import pairs_with_given_sum
import pytest
# example input 1:
# expected output 1:

# example input 2:
# expected output 2:

# example input 3:
# expected output 3:

# example input 4:
# expected output 4:

# example input 5:
# expected output 5:

# example input 6:
# expected output 6:

# test1
def test_raise_error_if_input_non_intiger():
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
def test_gives_number_of_pairs():
    # arrange
    numbers = [1, 2, 4, 5]
    target = 6
    expected = 2
    # act
    expected = pairs_with_given_sum(numbers, target)
    # assert
    assert expected == expected

# test4
def test_if_list_has_only_one_number_and_that_number_equal_to_target():
    # arrange
    numbers = [6]
    target = 6
    expected = 0
    # act
    expected = pairs_with_given_sum(numbers, target)
    # assert
    assert expected == expected

# test 5
def test_if_list_has_two_numbers_and_one_number_equal_to_target():
    # arrange
    numbers = [6, 0]
    target = 6
    expected = 1
    # act
    expected = pairs_with_given_sum(numbers, target)
    # assert
    assert expected == expected

# test 6
def test_if_the_input_of_numbers_is_none_integer():
    # arrange
    numbers = ['a', 'b', 'c']
    target = 6
    # act and assert
    with pytest.raises(ValueError):
        pairs_with_given_sum(numbers, target)