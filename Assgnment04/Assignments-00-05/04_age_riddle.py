"""
Program: Age Riddle
------------------
This program calculates and displays the ages of five friends
based on their relative age relationships.
"""

def main():
    anton = 21
    beth = anton + 6
    chen = beth + 20
    drew = chen + anton
    ethan = chen
    
    # Print everyone's ages
    print(f"Anton is {anton}")
    print(f"Beth is {beth}")
    print(f"Chen is {chen}")
    print(f"Drew is {drew}")
    print(f"Ethan is {ethan}")


if __name__ == '__main__':
    main()
