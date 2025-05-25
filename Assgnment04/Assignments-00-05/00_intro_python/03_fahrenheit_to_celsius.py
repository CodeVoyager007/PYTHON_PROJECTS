"""
Program: Temperature Converter
----------------------------
This program converts a temperature from Fahrenheit to Celsius
using the formula: celsius = (fahrenheit - 32) * 5.0/9.0
"""

def main():
    # Get temperature in Fahrenheit from user
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    
    # Convert to Celsius
    celsius = (fahrenheit - 32) * 5.0/9.0
    
    # Display the result
    print(f"\nTemperature: {fahrenheit}F = {celsius}C")


if __name__ == '__main__':
    main()
