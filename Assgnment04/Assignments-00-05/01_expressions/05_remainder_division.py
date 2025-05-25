def main():
    # Get the first number (dividend)
    dividend_str = input("Please enter an integer to be divided: ")
    dividend = int(dividend_str)
    
    # Get the second number (divisor)
    divisor_str = input("\nPlease enter an integer to divide by: ")
    divisor = int(divisor_str)
    
    # Calculate quotient and remainder
    quotient = dividend // divisor
    remainder = dividend % divisor
    
    # Print the result
    print(f"\nThe result of this division is {quotient} with a remainder of {remainder}")

if __name__ == '__main__':
    main()
