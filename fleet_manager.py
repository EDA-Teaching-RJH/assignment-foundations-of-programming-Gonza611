def init_database():
    names = ["Jean-Luc Picard", "William Riker", "Data", "Worf", "Geordi La Forge"]
    ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Lieutenant"]
    divs = ["Command", "Command", "Operations", "Security", "Operations"]
    ids = [1001, 1002, 1003, 1004, 1005]

    return names, ranks, divs, ids

def display_menu(user):
    print("\nFleet Manager")
    print("Logged in as:", user)
    print("1. Add Member")
    print("2. Remove Member")
    print("3. Update Rank")
    print("4. Display Roster")
    print("5. Search Crew")
    print("6. Filter by Division")
    print("7. Calculate Payroll")
    print("8. Count Officers")
    print("9. Exit")

    return input("Select option: ")

def main():
    names, ranks, divs, ids = init_database()

    user = input("Enter your full name: ")

    while True:
        choice = display_menu(user)

        if choice == "9":
            print("Exiting system.")
            break

if __name__ == "__main__":
    main()
