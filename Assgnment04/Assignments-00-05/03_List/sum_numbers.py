def calculate_sum(numbers: list[int]) -> int:
    """
    Calculates the sum of all numbers in a list using Python's built-in sum function.
    Args:
        numbers: A list of integers to sum
    Returns:
        The total sum of all numbers
    """
    return sum(numbers)

def main():
    # Test with different number lists
    test_numbers = [10, 20, 30, 40, 50]
    result = calculate_sum(test_numbers)
    print(f"The sum of {test_numbers} is: {result}")
    
    # Additional test case
    more_numbers = [1, -2, 3, -4, 5]
    result2 = calculate_sum(more_numbers)
    print(f"The sum of {more_numbers} is: {result2}")

if __name__ == '__main__':
    main() 