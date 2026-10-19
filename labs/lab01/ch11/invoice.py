# Starting file for Lab 1 Chapter 11 invoice.py program
# Name: Temitope Olugbemi
# Date: 10-18-2026
# Class: Dev 128

from datetime import datetime, timedelta

def get_invoice_date():
    while True:
        invoice_date_str = input("Enter the invoice date (MM/DD/YYYY): ")    
        try:
            invoice_date = datetime.strptime(invoice_date_str, "%m/%d/%Y")
        except ValueError:
            print("Invalid date format! Try again.")
            print()
            continue

        today = datetime.now();
        if today < invoice_date:
            print("Date must be today or earlier. Try again.")
            print()
        else:
            return invoice_date

def main():
    print("The Invoice Due Date program")
    print()

    again = "y"
    while again.lower() == "y":
        invoice_date = get_invoice_date()
        print()

        # calculate due date and days overdue
        due_date = invoice_date + timedelta(days=30)
        current_date = datetime.now()
        days_overdue = (current_date - due_date).days

        # display results
        date_format = "%B %d, %Y"
        print(f"Invoice Date: {invoice_date:{date_format}}")
        print(f"Due Date:     {due_date:{date_format}}")
        print(f"Current Date: {current_date:{date_format}}")
        if days_overdue > 0:
            print(f"This invoice is {days_overdue} day(s) overdue.")
        else:
            days_due = days_overdue * -1
            print(f"This invoice is due in {days_due} day(s).")
        print()

        # ask if user wants to continue
        while True:
            again = input("Continue? (y/n): ").strip().lower()
            if again in ("y", "n"):
                break
            print("Invalid input. Enter y or n.")
            print()
        
    print("Bye!")      

if __name__ == "__main__":
    main()
