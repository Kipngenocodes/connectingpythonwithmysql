# import tkinter module
import tkinter as tk

import mysql.connector

# creating a window
root = tk.Tk()
# creating windows title
root.title("Users Information.")
# Giving the window geometry
root.geometry("500x500")

# Creatig a databasewhich will keep all our prsonal data
mydatabase = mysql.connector.connect(
    host="localhost",
    user="root",
    password='Kapsabet',
    port="3306",
    database="Workingwithpython"
)


# creating a submit function which will get our imput to database
def submit():
    # connecting to an existing database to store information which is being input by the user:
    mydatabase = mysql.connector.connect(
        host="localhost",
        user="root",
        password='Kapsabet',
        port="3306",
        database="Workingwithpython"
    )

    # creation of cursor which allows us to send command to database  to do something.
    mycursor = mydatabase.cursor()

    # insert into table from the entry widget
    msql_insertion = ("INSERT INTO Personal_information("
                     "Firstname,"
                     " Lastname,"
                     " mail,"
                     "Phonenumber,"
                     "Street_Address,"
                     "City,"
                     "State,"
                     "Zipcode) "
                     "values (%s,%s,%s,%s,%s,%s,%s,%s)")

    data = (
        firstname_entry.get(),
        lastname_entry.get(),
        email_entry.get(),
        phonenumber_entry.get(),
        street_address_entry.get(),
        city_entry.get(),
        state_entry.get(),
        zip_code_entry.get()
    )

    mycursor.execute(msql_insertion, data)

    # commiting changes to database
    mydatabase.commit()

    # closing the  connection upon completing using the database.
    mydatabase.close()
    # Clear the entry widget
    firstname_entry.delete(0, "end"),
    lastname_entry.delete(0, "end"),
    email_entry.delete(0, "end"),
    phonenumber_entry.delete(0, "end"),
    street_address_entry.delete(0, "end"),
    city_entry.delete(0, "end"),
    state_entry.delete(0, "end"),
    zip_code_entry.delete(0, "end")


def show_value():
    # connecting to an existing database to query and display information which have been input by the user:
    mydatabase = mysql.connector.connect(
        host="localhost",
        user="root",
        password='Kapsabet',
        port="3306",
        database="Workingwithpython"
    )

    # creation of cursor which allows us to send command to database  to do something.
    mycursor = mydatabase.cursor()

    # selecting data from th database
    mycursor.execute(f"SELECT *, personal_id FROM Personal_information")

    # allows fetching from the database
    myresult = mycursor.fetchall()

    '''create variable print_myresult and equate it to an empty string where the data will be displayed.
    Dataretrival process from the database'''
    print_myresult = " "

    # creation of a for loop to loop the query
    for results in myresult:
        print_myresult += str(results) +"\n"
    # printing output from our database
    print(print_myresult)

    mycursor.close()
    mydatabase.close()



# Creating a function to which is binded to update button

def update():
    top = tk.Toplevel(root)
    top.geometry("500x500")
    top.title(" Update Users Information")

    # creating labels for the update page
    firstname_label = tk.Label(top, text="First Name", padx=10, pady=10)
    firstname_label.grid(row=0, column=0)
    lastname_label = tk.Label(top, text="Last Name", padx=10, pady=10)
    lastname_label.grid(row=1, column=0)
    email_label = tk.Label(top, text="Email Address", padx=10, pady=10)
    email_label.grid(row=2, column=0)
    phonenumber_label = tk.Label(top, text="Phone Number", padx=10, pady=10)
    phonenumber_label.grid(row=3, column=0)
    street_address_label = tk.Label(top, text="Address", padx=10, pady=10)
    street_address_label.grid(row=4, column=0)
    city_label = tk.Label(top, text="City", padx=10, pady=10)
    city_label.grid(row=5, column=0)
    state_label = tk.Label(top, text="State", padx=10, pady=10)
    state_label.grid(row=6, column=0)
    zip_code_label = tk.Label(top, text="Zip", padx=10, pady=10)
    zip_code_label.grid(row=7, column=0)

    # creating entry boxes for update information
    firstname_entry = tk.Entry(top)
    firstname_entry.grid(row=0, column=1)

    lastname_entry = tk.Entry(top)
    lastname_entry.grid(row=1, column=1)

    email_entry = tk.Entry(top)
    email_entry.grid(row=2, column=1)

    phonenumber_entry = tk.Entry(top)
    phonenumber_entry.grid(row=3, column=1)

    street_address_entry = tk.Entry(top)
    street_address_entry.grid(row=4, column=1)

    city_entry = tk.Entry(top)
    city_entry.grid(row=5, column=1)

    state_entry = tk.Entry(top)
    state_entry.grid(row=6, column=1)

    zip_code_entry = tk.Entry(top)
    zip_code_entry.grid(row=7, column=1)

    # Creating Button which  when commanded, it links with databse to update information
    sbutton = tk.Button(top, text="Submit")
    sbutton.grid(row=8, column=1)

    root.mainloop()


# creating labels for the login page
firstname_label = tk.Label(root, text="First Name", padx=10, pady=10)
firstname_label.grid(row=0, column=0)
lastname_label = tk.Label(root, text="Last Name", padx=10, pady=10)
lastname_label.grid(row=1, column=0)
email_label = tk.Label(root, text="Email Address", padx=10, pady=10)
email_label.grid(row=2, column=0)
phonenumber_label = tk.Label(root, text="Phone Number", padx=10, pady=10)
phonenumber_label.grid(row=3, column=0)
street_address_label = tk.Label(root, text="Address", padx=10, pady=10)
street_address_label.grid(row=4, column=0)
city_label = tk.Label(root, text="City", padx=10, pady=10)
city_label.grid(row=5, column=0)
state_label = tk.Label(root, text="State", padx=10, pady=10)
state_label.grid(row=6, column=0)
zip_code_label = tk.Label(root, text="Zip", padx=10, pady=10)
zip_code_label.grid(row=7, column=0)

# Creation of a  button to add data values to database

update_value_label = tk.Label(root, text="Value", padx=10, pady=10)
update_value_label.grid(row=9, column=0)

# creating entry boxes
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

# creating a button to add data to a database which
submit_button = tk.Button(text="Submit", command=submit)
submit_button.grid(row=8, column=1, padx=10, pady=3, ipadx=50)

# This is the entry button which you can imput the ID which need to be updated or deleted
value_button = tk.Entry()
value_button.grid(row=9, column=1)

# creating update button which when clicked it leads to update page
update_button = tk.Button(root, text="Update", command=update)
update_button.grid(row=10, column=1, padx=10, pady=3, ipadx=50)

# Creating a button to submit what is being updated.
delete_button = tk.Button(text="delete", command="")
delete_button.grid(row=11, column=1, padx=10, pady=5, ipadx=50)

# Creating a button to show button to display what is in the database
show_button = tk.Button(root, text="show", command=show_value)
show_button.grid(row=12, column=1, padx=10, pady=5, ipadx=50)

root.mainloop()
