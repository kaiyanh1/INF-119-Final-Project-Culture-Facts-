import os
import culture_service

def display_menu():
    print("\nCulture Facts App")
    print("1. List all cultures")
    print("2. Search for a culture")
    print("3. Get a random cultural fact")
    print("4. Get details about a culture")
    print("5. Quit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            cultures = culture_service.list_cultures()
            if cultures:
                print("\nList of Cultures:")
                for culture in cultures:
                    print(f"- {culture}")
            else:
                print("Error: Could not retrieve cultures.")

        elif choice == '2':
            name = input("Enter the name of the culture to search for: ")
            culture = culture_service.search_culture(name)
            if culture:
                print(f"\nCulture found: {culture['name']}")
                print(f"Region: {culture['region']}")
                print(f"Description: {culture['description']}")
            else:
                print("Culture not found.")

        elif choice == '3':
            fact = culture_service.get_random_fact()
            if fact:
                print(f"\nRandom Cultural Fact: {fact}")
            else:
                print("Error: Could not retrieve a random fact.")

        elif choice == '4':
            name = input("Enter the name of the culture to get details for: ")
            details = culture_service.get_details(name)
            if details:
                print(f"\nDetails for {details['name']}:")
                print(f"Region: {details['region']}")
                print(f"Description: {details['description']}")
                print("Facts:")
                for fact in details['facts']:
                    print(f"- {fact}")
                print("Traditions:")
                for tradition in details['traditions']:
                    print(f"- {tradition}")
            else:
                print("Culture not found.")

        elif choice == '5':
            print("Exiting Culture Facts App. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()