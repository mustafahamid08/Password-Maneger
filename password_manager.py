import csv
import os
import random
import string

FILE_NAME = "passwords.csv"


def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Website", "Username", "Password"])


def generate_password():
    characters = string.ascii_letters + string.digits + string.punctuation

    password = "".join(random.choice(characters) for _ in range(12))

    print("\nGenerated Password:", password)

    return password


def add_password():
    website = input("Enter Website: ")
    username = input("Enter Username/Email: ")

    choice = input("Generate Password? (y/n): ").lower()

    if choice == "y":
        password = generate_password()
    else:
        password = input("Enter Password: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([website, username, password])

    print("Password Saved Successfully!")


def view_passwords():
    print("\n===== SAVED PASSWORDS =====\n")

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            print(row)


def search_website():
    website = input("Enter Website Name: ")

    found = False

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["Website"].lower() == website.lower():
                print("\nWebsite Found:")
                print(row)
                found = True

    if not found:
        print("No Record Found.")


def main():
    initialize_file()

    while True:
        print("\n===== PASSWORD MANAGER =====")
        print("1. Add Password")
        print("2. View Passwords")
        print("3. Search Website")
        print("4. Generate Password")
        print("5. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            add_password()

        elif choice == "2":
            view_passwords()

        elif choice == "3":
            search_website()

        elif choice == "4":
            generate_password()

        elif choice == "5":
            print("Thank You For Using Password Manager!")
            break

        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()