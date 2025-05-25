def main():
    # Get feet input from user
    feet_str = input("Enter number of feet: ")
    feet = float(feet_str)
    
    # Convert feet to inches (12 inches per foot)
    inches = feet * 12
    
    # Print the result
    print(f"{feet} feet = {inches} inches")

if __name__ == '__main__':
    main()
