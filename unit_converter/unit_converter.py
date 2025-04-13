def km_to_miles(km):
    return km * 0.621371

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def main_menu():
    while True:
        print("\n== Unit Converter ==")
        print("1: Kilometers to Miles")
        print("2: Celsius to Fahrenheit")
        print("3: Exit")
        choice = input("Select an option (1-3): ")

        if choice == "1":
            km = float(input("Enter kilometers: "))
            print(f"{km} km is equal to {km_to_miles(km):.2f} miles.")
        elif choice == "2":
            c = float(input("Enter Celsius: "))
            print(f"{c}°C is equal to {celsius_to_fahrenheit(c):.2f}°F.")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()