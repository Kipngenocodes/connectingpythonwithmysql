# import tkinter module
import tkinter as tk
import mysql.connector


# creating a window
root = tk.Tk()
# creating windows title
root.title("Users Information.")
# Giving the window geometry
root.geometry("500x500")



# Creating a function to which is binded to update button

def update ():
    top = tk.Toplevel(root)
    top.geometry("500x500")
    top.title(" Update Users Information")

    root.mainloop()

# creating labels for the login page
firstname_label = tk.Label (root, text="First Name",padx=10, pady=10)
firstname_label.grid(row=0, column=0)
lastname_label = tk.Label(root, text="Last Name",padx=10, pady=10)
lastname_label.grid(row=1, column=0)
email_label = tk.Label(root, text="Email Address",padx=10, pady=10)
email_label.grid(row=2, column=0)
phonenumber_label = tk.Label(root, text="Phone Number", padx=10, pady=10)
phonenumber_label.grid(row=3, column=0)
street_address_label = tk.Label(root, text="Address", padx=10, pady=10)
street_address_label.grid(row=4, column=0)
city_label = tk.Label(root, text="City", padx=10, pady=10)
city_label.grid(row=5, column=0)
state_label = tk.Label(root, text="State",padx=10, pady=10)
state_label.grid(row=6, column=0)
zip_code_label = tk.Label(root, text="Zip", padx=10, pady=10)
zip_code_label.grid(row=7, column=0)

#creating entry boxes
firstname_entry = tk.Entry()
firstname_entry.grid(row=0, column=1)

lastname_entry = tk.Entry()
lastname_entry.grid(row=1, column=1)

email_entry = tk.Entry()
email_entry.grid(row=2, column=1)

phonenumber_entry = tk.Entry()
phonenumber_entry.grid(row=3, column=1)

street_address_entry = tk.Entry()
street_address_entry.grid(row=4, column=1)

city_entry = tk.Entry()
city_entry.grid(row=5, column=1)

state_entry = tk.Entry()
state_entry.grid(row=6, column=1)

zip_code_entry = tk.Entry()
zip_code_entry.grid(row=7, column=1)

update_delete_button = tk.Entry()
update_delete_button.grid(row=8, column=1)

# creating update, delete and submit button
update_button = tk.Button(root, text="Update", command=update)
update_button.grid(row=9, column=1, ipadx=40)

submit_button = tk.Button(text="Submit")
submit_button.grid(row=10, column=1, ipadx=40)




root.mainloop()
