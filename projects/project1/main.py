# Starting file for Project 1
# Name: Temitope S. Olugbemi
# Date: 11-12-2026
# Class: Dev 128

import csv
import sqlite3
from pathlib import Path

def setup_database(conn, cursor):
    """Create the user table if it doesn't exist and seed it from the CSV when empty."""
    # 1. Database Design & Persistence: (CREATE TABLE IF NOT EXISTS, no DROP TABLE)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user (
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            phone TEXT NOT NULL UNIQUE,
            street_address TEXT NOT NULL,
            city TEXT NOT NULL,
            state TEXT NOT NULL,
            zip_code TEXT NOT NULL,
            PRIMARY KEY (email, phone)
        )
    ''')

    # 2. Checks if the table is empty to avoid duplicating seed data on re-runs
    cursor.execute('SELECT COUNT(*) FROM user')
    if cursor.fetchone()[0] == 0:
        csv_path = Path(__file__).with_name("initial_users.csv")
        with open(csv_path, newline="", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            columns = (
                "first_name",
                "last_name",
                "email",
                "phone",
                "street_address",
                "city",
                "state",
                "zip_code",
            )
            initial_users = [tuple(row[column] for column in columns) for row in reader]

        cursor.executemany(
            """
            INSERT INTO user (
                first_name, last_name, email, phone,
                street_address, city, state, zip_code
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            initial_users,
        )

    conn.commit()


    # Verify that the table has been created and seeded
    cursor.execute('SELECT COUNT(*) FROM user')
    user_count = cursor.fetchone()[0]
    print(f"Database setup completed! User table has {user_count} records.\n")


def list_all_names(cursor):
    """Option 1: List all first and last names in the user table."""
    print("\nAll NAMES in the USER table")
    print("-" * 30)
    cursor.execute("SELECT first_name, last_name FROM user")
    users = cursor.fetchall()
    for user in users:
        print(f"{user[0]} {user[1]}")
    print()


def list_names_contact(cursor):
    """Option 2: List all first and last names with their email and phone number."""
    print("\nNAMES with EMAIL and PHONE in the USER table")
    print("-" * 50)
    cursor.execute("SELECT first_name, last_name, email, phone FROM user")
    users = cursor.fetchall()
    for user in users:
        print(f"{user[0]} {user[1]} - Email: {user[2]}, Phone: {user[3]}")
    print()


def list_names_location(cursor):
    """Option 3: List all first and last names with their city and state."""
    print("\nNAMES with CITY and STATE in the USER table")
    print("-" * 50)
    cursor.execute("SELECT first_name, last_name, city, state FROM user")
    users = cursor.fetchall()
    for user in users:
        print(f"{user[0]} {user[1]} - City: {user[2]}, State: {user[3]}")
    print()


def add_new_user(conn, cursor):
    """Option 4: Add a new user to the database."""
    print("\nAdd a New User")
    print("-" * 20)
    first_name = input("Enter first name: ").strip()
    last_name = input("Enter last name: ").strip()
    email = input("Enter email: ").strip()
    phone = input("Enter phone number: ").strip()
    street_address = input("Enter street address: ").strip()
    city = input("Enter city: ").strip()
    state = input("Enter 2 digit state abbreviation: ").strip()
    zip_code = input("Enter zip code: ").strip()

    try:
        cursor.execute(
            """
            INSERT INTO user (
                first_name, last_name, email, phone,
                street_address, city, state, zip_code
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (first_name, last_name, email, phone, street_address, city, state, zip_code),
        )
        conn.commit()
        print(f"User {first_name} {last_name} added successfully!\n")
    except sqlite3.IntegrityError as e:
        print(f"Error adding user: {e}\n")


def main():
    print("Welcome to the Marvel Universe User Management System\n")

    # Connect to the SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # Setup the database and seed it if necessary
    setup_database(conn, cursor)

    while True:
        print("** Main Menu ***\n")
        print("1. List all names")
        print("2. List names with contact information")
        print("3. List names with location information")
        print("4. Add a new user")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            list_all_names(cursor)
        elif choice == "2":
            list_names_contact(cursor)
        elif choice == "3":
            list_names_location(cursor)
        elif choice == "4":
            add_new_user(conn, cursor)
        elif choice == "5":
            print("Exiting the program... Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.\n")

    # Close the database connection before exiting
    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()