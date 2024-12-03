import datetime
from tkinter import messagebox

# Function to save customer booking information to the file
def save_booking_to_file(customer_name, contact_number, num_persons, table_number, customer_type):
    try:
        # Get the current time of the booking
        booking_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        
        # Set default priority based on customer type
        if customer_type == "Walk-in":
            priority = 3  # Walk-in customers get priority 3
        else:
            priority = 1  # Default priority for other customers (VIP/Regular)

        # Open the file to append the booking details
        with open("bookings.txt", "a") as file:
            file.write(f"Name: {customer_name}, Contact: {contact_number}, Persons: {num_persons}, "
                       f"Table No: {table_number}, Priority: {priority}, Booking Time: {booking_time}, "
                       f"Customer Type: {customer_type}\n")
        
        # Show a confirmation message
        messagebox.showinfo("Booking Successful", f"Booking confirmed for Table No: {table_number}.\nYour reservation is recorded!")
    
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while saving the booking: {str(e)}")

# Function to handle Walk-in customer
def handle_walk_in():
    # Input for Walk-in customer (customer details)
    customer_name = input("Enter Customer Name: ")
    contact_number = input("Enter Contact Number: ")
    num_persons = int(input("Enter Number of Persons: "))
    
    # Check table availability from a predefined list or system (simulated here)
    available_tables = [1, 2, 3, 4, 5]  # Simulated list of available tables
    
    if available_tables:
        table_number = available_tables[0]  # Assign the first available table
        # Remove assigned table from available list (if needed)
        available_tables.remove(table_number)
        
        # Save booking details to file with 'Walk-in' as customer type
        save_booking_to_file(customer_name, contact_number, num_persons, table_number, "Walk-in")
    else:
        print("Sorry, no tables available for Walk-in customers right now.")
    
# Example of saving VIP/Regular customer info to the file (you can call this function elsewhere as needed)
def handle_booking():
    # Input for regular or VIP customer
    customer_name = input("Enter Customer Name: ")
    contact_number = input("Enter Contact Number: ")
    num_persons = int(input("Enter Number of Persons: "))
    
    # Check table availability from a predefined list or system (simulated here)
    available_tables = [1, 2, 3, 4, 5]  # Simulated list of available tables
    
    if available_tables:
        table_number = available_tables[0]  # Assign the first available table
        # Remove assigned table from available list (if needed)
        available_tables.remove(table_number)
        
        # Choose customer type (Regular/VIP) and save to file
        customer_type = input("Enter Customer Type (Regular/VIP): ")
        save_booking_to_file(customer_name, contact_number, num_persons, table_number, customer_type)
    else:
        print("Sorry, no tables available for booking right now.")
