def double_list(numbers: list[int]) -> list[int]:
    """
    Creates a new list with each number doubled using list comprehension.
    Args:
        numbers: List of integers to double
    Returns:
        A new list with all numbers doubled
    """
    return [num * 2 for num in numbers]

def main():
    # Test case 1: Simple positive numbers
    test_list = [5, 10, 15, 20]
    doubled = double_list(test_list)
    print(f"Original list: {test_list}")
    print(f"Doubled list: {doubled}")
    
    # Test case 2: Mixed positive and negative numbers
    mixed_list = [-3, 0, 7, -2, 8]
    doubled_mixed = double_list(mixed_list)
    print(f"\nOriginal mixed list: {mixed_list}")
    print(f"Doubled mixed list: {doubled_mixed}")

if __name__ == '__main__':
    main() 