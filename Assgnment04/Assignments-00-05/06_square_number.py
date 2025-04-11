"""
Program: Number Squarer
----------------------
This program takes a number as input and displays its square.
"""
# Get input
def main():
    # Get input
    number = float(input("Type a number to see its square: "))
    
    # Calculate 
    square = number ** 2
    
    # result
    print(f"\n{number} squared is {square}")


if __name__ == '__main__':
    main()
