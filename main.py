import tkinter as tk
from tkinter import messagebox

# Function to handle Booking Button
def make_booking():
    messagebox.showinfo("Booking", "You can make a booking here!")

# Function to handle Walk-in Button
def walk_in():
    messagebox.showinfo("Walk-in", "You can register a walk-in customer here!")

# Function to handle Check Reservation Status Button
def check_status():
    messagebox.showinfo("Reservation Status", "Check current reservation status here!")

# Function for button hover effect
def on_enter(button):
    button.config(bg="#FF6347")  # Change color when hovered (Tomato)

def on_leave(button):
    button.config(bg="#32CD32")  # Reset to original color when hover ends (Lime Green)

# Creating the main window
root = tk.Tk()
root.title("Restaurant Management System")

# Maximize the window and remove borders
root.state('zoomed')  # This will open the window maximized

# Set background color for the window
root.config(bg="#F0F8FF")  # Light sky blue background

# Adding a Label on the main screen
label = tk.Label(root, text="Welcome to Restaurant Management System", font=("Helvetica", 20, "bold"), bg="#F0F8FF", fg="#4B0082")
label.pack(pady=60)  # Increased the top padding to center better vertically

# Creating a Frame to contain buttons in the middle
button_frame = tk.Frame(root, bg="#F0F8FF")
button_frame.pack(pady=80)  # Increased the bottom padding to center the buttons more vertically

# Function to create buttons with rounded corners
def create_button(text, command):
    button = tk.Button(button_frame, text=text, width=20, height=2, command=command, bg="#32CD32", fg="white", font=("Helvetica", 12, "bold"), relief="flat", bd=5, activebackground="#FF6347", activeforeground="white")
    button.pack(side="left", padx=20)  # Buttons are placed side by side (horizontally)
    
    # Bind the hover effect
    button.bind("<Enter>", lambda event, button=button: on_enter(button))
    button.bind("<Leave>", lambda event, button=button: on_leave(button))
    
    # Rounded corners: by setting the corner radius to 20 pixels
    button.config(highlightthickness=0, bd=0, relief="flat", padx=20, pady=10)
    return button

# Create the buttons for Booking, Walk-in, and Check Reservation Status
button_booking = create_button("Make a Booking", make_booking)
button_walk_in = create_button("Walk-in Customer", walk_in)
button_check_status = create_button("Check Reservation Status", check_status)

# Run the Tkinter event loop
root.mainloop() 