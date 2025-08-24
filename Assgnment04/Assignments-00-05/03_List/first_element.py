def get_first_element(lst: list) -> None:
    """
    Safely prints the first element of a list with error handling.
    Args:
        lst: Input list to process
    """
    try:
        if not lst:
            print("Error: The list is empty!")
            return
        print(f"The first element is: {lst[0]}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Interactive input
    print("Enter elements one by one (press Enter twice to finish):")
    elements = []
    
    while True:
        element = input("Enter an element (or press Enter to finish): ")
        if not element:
            break
        elements.append(element)
    
    # Test the function
    print("\nYour list:", elements)
    get_first_element(elements)
    
    # Additional test cases
    print("\nTesting with empty list:")
    get_first_element([])

if __name__ == '__main__':
    main() 