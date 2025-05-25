"""
Program: Triangle Perimeter Calculator
-----------------------------------
This program calculates the perimeter of a triangle
by taking three side lengths as input from the user.
"""

def main():
    side1 = float(input("What is the length of side 1? "))
    side2 = float(input("What is the length of side 2? "))
    side3 = float(input("What is the length of side 3? "))
    
    # Calculate perimeter
    perimeter = side1 + side2 + side3
    
    #display result
    print(f"\nThe perimeter of the triangle is {perimeter}")


if __name__ == '__main__':
    main()
