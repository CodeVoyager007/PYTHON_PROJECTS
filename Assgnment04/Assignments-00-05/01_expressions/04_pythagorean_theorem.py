import math

def main():
    # Get the lengths of the two perpendicular sides
    ab_str = input("Enter the length of AB: ")
    ac_str = input("\nEnter the length of AC: ")
    
    # Convert strings to floats
    ab = float(ab_str)
    ac = float(ac_str)
    
    # Calculate hypotenuse using Pythagorean theorem
    bc = math.sqrt(ab**2 + ac**2)
    
    # Print the result
    print(f"\nThe length of BC (the hypotenuse) is: {bc}")

if __name__ == '__main__':
    main()
