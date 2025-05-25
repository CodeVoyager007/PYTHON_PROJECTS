def main():
    # Speed of light constant in meters per second
    C = 299792458
    
    # Get mass input from user
    mass_str = input("Enter kilos of mass: ")
    mass = float(mass_str)
    
    print("\ne = m * C^2...")
    print(f"\nm = {mass} kg")
    print(f"\nC = {C} m/s")
    
    # Calculate energy using E = mc^2
    energy = mass * (C ** 2)
    
    print(f"\n{energy} joules of energy!")

if __name__ == '__main__':
    main()
