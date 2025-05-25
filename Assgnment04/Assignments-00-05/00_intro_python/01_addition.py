"""
Program: Addition Calculator
--------------------------
This program takes two numbers as input from the user
and calculates their sum.
"""

def main():
    # Welcome message
    print("Welcome to the Addition Calculator!")
    
   
    first_number = int(input("Please enter the first number: "))
 
    second_number = int(input("Please enter the second number: "))
    
    result = first_number + second_number
    
    
    print(f"The sum of {first_number} and {second_number} is {result}")


if __name__ == '__main__':
    main()
