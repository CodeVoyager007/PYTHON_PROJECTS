def main():
    # The start of our sentence
    SENTENCE_START = "Code in Place is fun. I learned to program and used Python to make my"
    
    # Get words from user
    adjective = input("Please type an adjective and press enter. ")
    noun = input("\nPlease type a noun and press enter. ")
    verb = input("\nPlease type a verb and press enter. ")
    
    # Create and print the final sentence
    print(f"\n{SENTENCE_START} {adjective} {noun} {verb}!")

if __name__ == '__main__':
    main()
