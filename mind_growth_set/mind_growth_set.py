from colorama import Fore, init

# Initialize colorama for colorful text
init(autoreset=True)

def daily_quote():
    print(Fore.CYAN + "\n🌟 Daily Quote 🌟")
    print(Fore.YELLOW + "\"The best way to predict your future is to create it.\"")

def challenges():
    print(Fore.GREEN + "\n💪 Today's Challenges 💪")
    activities = [
        "Write down three things you're grateful for.",
        "Learn something new for 15 minutes.",
        "Reflect on a recent challenge and how you overcame it."
    ]
    for index, activity in enumerate(activities, 1):
        print(f"{index}. {activity}")

def reflect():
    print(Fore.MAGENTA + "\n📔 Self-Reflection 📔")
    response = input("What are you proud of today? ")
    print(Fore.YELLOW + f"Keep it up! Reflection saved: \"{response}\".")

def main_menu():
    while True:
        print(Fore.BLUE + "\n== Mind Growth Set Menu ==")
        print("1: Show Daily Quote")
        print("2: View Challenges")
        print("3: Reflect on the Day")
        print("4: Exit")
        choice = input(Fore.WHITE + "Select an option (1-4): ")

        if choice == "1":
            daily_quote()
        elif choice == "2":
            challenges()
        elif choice == "3":
            reflect()
        elif choice == "4":
            print(Fore.LIGHTGREEN_EX + "Goodbye! Stay positive!")
            break
        else:
            print(Fore.RED + "Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()