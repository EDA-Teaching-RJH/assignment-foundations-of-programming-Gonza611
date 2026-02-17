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

def display_roster(names, ranks, divs, ids):
    print("\n--- Crew Roster ---")
    print("ID\tName\t\t\tRank\t\tDivision")
    print("-" * 60)

    for i in range(len(names)):
        print(ids[i], "\t", names[i], "\t", ranks[i], "\t", divs[i])

def count_officers(ranks):
    count = 0

    for rank in ranks:
        if rank == "Captain" or rank == "Commander":
            count += 1

    return count

def calculate_payroll(ranks):
    total = 0

    for rank in ranks:
        if rank == "Captain":
            total += 1000
        elif rank == "Commander":
            total += 800
        elif rank == "Lt. Commander":
            total += 600
        elif rank == "Lieutenant":
            total += 400
        elif rank == "Ensign":
            total += 200

    return total

def search_crew(names, ranks, divs, ids):
    term = input("Enter name to search: ").lower()

    found = False

    for i in range(len(names)):
        if term in names[i].lower():
            print(ids[i], "-", names[i], "-", ranks[i], "-", divs[i])
            found = True

    if not found:
        print("No crew member found.")

def filter_by_division(names, divs):
    division = input("Enter division (Command, Operations, Security, Sciences): ")

    found = False

    for i in range(len(names)):
        if divs[i] == division:
            print(names[i], "-", divs[i])
            found = True

    if not found:
        print("No crew members found in that division.")

def add_member(names, ranks, divs, ids):
    new_id = int(input("Enter new ID: "))

    if new_id in ids:
        print("ID already exists.")
        return

    valid_ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Ensign"]

    new_rank = input("Enter Rank: ")
    if new_rank not in valid_ranks:
        print("Invalid rank.")
        return

    new_name = input("Enter Name: ")
    new_div = input("Enter Division: ")

    names.append(new_name)
    ranks.append(new_rank)
    divs.append(new_div)
    ids.append(new_id)

    print("Crew member added successfully.")

def main():
    names, ranks, divs, ids = init_database()

    user = input("Enter your full name: ")

    while True:
        choice = display_menu(user)

        if choice == "9":
            print("Exiting system.")
            break

        elif choice == "4":
            display_roster(names, ranks, divs, ids)

        elif choice == "8":
            total = count_officers(ranks)
            print("Number of senior officers:", total)

        elif choice == "7":
            total = calculate_payroll(ranks)
            print("Total crew payroll:", total, "credits")

        elif choice == "5":
            search_crew(names, ranks, divs, ids)

        elif choice == "6":
            filter_by_division(names, divs)

        elif choice == "1":
            add_member(names, ranks, divs, ids)






if __name__ == "__main__":
    main()
