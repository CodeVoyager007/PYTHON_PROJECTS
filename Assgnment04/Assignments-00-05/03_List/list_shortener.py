def shorten_list(lst: list, max_length: int = 3) -> list:
    """
    Shortens a list to the specified maximum length and returns removed elements.
    Args:
        lst: The list to shorten
        max_length: Maximum allowed length (default 3)
    Returns:
        List of removed elements in order of removal
    """
    if max_length < 0:
        raise ValueError("Maximum length cannot be negative")
        
    removed_elements = []
    while len(lst) > max_length:
        removed = lst.pop()
        removed_elements.append(removed)
        print(f"Removed: {removed}")
    
    return removed_elements

def main():
    # Get list from user
    elements = []
    print("Enter elements (press Enter with no input to finish):")
    
    while True:
        value = input("Add element: ")
        if not value:
            break
        elements.append(value)
    
    # Show initial state
    print(f"\nOriginal list: {elements}")
    print(f"Original length: {len(elements)}")
    
    # Get desired maximum length
    try:
        max_len = int(input("\nEnter maximum length (default is 3): ") or 3)
        
        # Shorten the list
        print("\nShortening process:")
        removed = shorten_list(elements, max_len)
        
        # Show results
        print(f"\nFinal list: {elements}")
        print(f"Final length: {len(elements)}")
        if removed:
            print(f"Removed elements (in order of removal): {removed}")
            print(f"Number of elements removed: {len(removed)}")
            
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main() 