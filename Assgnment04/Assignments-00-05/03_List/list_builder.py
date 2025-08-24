def build_list() -> list:
    """
    Builds a list from user input with additional features.
    Returns:
        The constructed list
    """
    elements = []
    print("Enter values to build your list!")
    print("Special commands:")
    print("  'done' - Finish building the list")
    print("  'undo' - Remove the last element")
    print("  'clear' - Clear the list")
    
    while True:
        current_list = f"Current list: {elements}"
        print("\n" + "=" * len(current_list))
        print(current_list)
        print("=" * len(current_list))
        
        value = input("\nEnter a value: ").strip()
        
        if not value:
            break
        elif value.lower() == 'done':
            break
        elif value.lower() == 'undo' and elements:
            removed = elements.pop()
            print(f"Removed: {removed}")
        elif value.lower() == 'clear':
            elements.clear()
            print("List cleared!")
        else:
            elements.append(value)
            
    return elements

def main():
    # Build the list
    final_list = build_list()
    
    # Display results
    print("\nFinal Results:")
    print(f"List contents: {final_list}")
    print(f"Number of elements: {len(final_list)}")
    if final_list:
        print(f"First element: {final_list[0]}")
        print(f"Last element: {final_list[-1]}")

if __name__ == '__main__':
    main() 