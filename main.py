# import tkinter module
import tkinter as tk
# importing the mysql connector to link to mysql database
import mysql.connector

# creating a window
root = tk.Tk()
# creating windows title
root.title("Users Information.")
# Giving the window geometry
root.geometry("500x500")

# Creatig a databasewhich will keep all our prsonal data
my_database = mysql.connector.connect(
    # location of the database
    host="localhost",
    # defining the user of the database
    user="root",
    # password for mysql workbench to access my database
    password='Kapsabet',
    # higligthing the port of the database
    port="3306",
    # defining or stating the database which all the table which will be used in the project
    database="Workingwithpython"
)


# creating a submit function which will get our imput to table  in the database
def submit():
    # connecting to an existing database to store information which is being input by the user:
    my_database = mysql.connector.connect(
        # location of the database
        host="localhost",
        # defining the user of the database
        user="root",
        # password for mysql workbench to access my database
        password='Kapsabet',
        # higligthing the port of the database
        port="3306",
        # defining or stating the database which all the table which will be used in the project
        database="Workingwithpython"
    )

    # creation or definition of cursor which allows us to send command to database to do something.
    mycursor = my_database.cursor()

    # insert into table from the entry widget
    msql_insertion = ("INSERT INTO personal_information("
                      "Firstname,"
                      " Lastname,"
                      "mail,"
                      "Phonenumber,"
                      "Street_Address,"
                      "City,"
                      "State,"
                      "Zipcode) "
                      "values (%s,%s,%s,%s,%s,%s,%s,%s)")
    # facilitate the attaching data whih was input by the user and gettig tem to database
    user_data = (
        firstname_entry.get(),
        lastname_entry.get(),
        email_entry.get(),
        phonenumber_entry.get(),
        street_address_entry.get(),
        city_entry.get(),
        state_entry.get(),
        zip_code_entry.get()
    )

    # Exeuting a command on the database to get user data.
    mycursor.execute(msql_insertion, user_data)

    # commiting changes to database
    my_database.commit()

    # closing the  connection upon completing using the database.
    my_database.close()
    # Clear the entry widget so next input can be inpute without any problem
    firstname_entry.delete(0, "end"),
    lastname_entry.delete(0, "end"),
    email_entry.delete(0, "end"),
    phonenumber_entry.delete(0, "end"),
    street_address_entry.delete(0, "end"),
    city_entry.delete(0, "end"),
    state_entry.delete(0, "end"),
    zip_code_entry.delete(0, "end")



def update_func():
    my_database = mysql.connector.connect(
        # location of the database
        host="localhost",
        # defining the user of the database
        user="root",
        # password for mysql workbench to access my database
        password='Kapsabet',
        # higligthing the port of the database
        port="3306",
        # defining or stating the database which all the table which will be used in the project
        database="Workingwithpython"
    )
    '''creation of cursor which allows us to send command to database 
        to process data returned by an SQL query, one row at a time.'''
    mycursor = my_database.cursor()
    myrecord = value_button.get()

    # Update data from the database
    updatequery=(""" 
    UPDATE personal_information SET 
         
        Firstname=%s,
        Lastname=%s,
        mail=%s,
        Phonenumber=%s,
        Street_Address=%s,
        City=%s,
        State=%s,
        Zipcode=%s
        
     where Personal_id =%s""")

    data_updater =(
        firstname_entry.get(),
        lastname_entry.get(),
        email_entry.get(),
        phonenumber_entry.get(),
        street_address_entry.get(),
        city_entry.get(),
        state_entry.get(),
        zip_code_entry.get(),
        myrecord
    )
    mycursor.execute(updatequery, data_updater)

    my_database.commit()

    mycursor.close()

    my_database.close()


def show_value():
    # creating a tkinter Window to faclitate the viewing results in another window
    showvalue = tk.Toplevel(root)
    # Defining the geometry of the show value window
    showvalue.geometry("500x500")
    # Defining the title of the show value window
    showvalue.title("Database Information")
    # connecting to an existing database to query and display information which have been input by the user:
    my_database = mysql.connector.connect(
        # location of the database
        host="localhost",
        # defining the user of the database
        user="root",
        # password for mysql workbench to access my database
        password='Kapsabet',
        # higligthing the port of the database
        port="3306",
        # defining or stating the database which all the table which will be used in the project
        database="Workingwithpython"
    )

    '''creation of cursor which allows us to send command to database 
    to process data returned by an SQL query, one row at a time.'''
    mycursor = my_database.cursor()

    # selecting data from th database
    mycursor.execute(f"SELECT * FROM Personal_information")

    # allows fetching from the mysql query
    myresult = mycursor.fetchall()

    # Update Tkinter widgets with the retrieved data (replace with your specific widget update logic)
    for row_index, row_data in enumerate(myresult):
        for col_index, col_value in enumerate(row_data):
            result_label = tk.Label(showvalue, text=col_value)
            result_label.grid(row=row_index, column=col_index)

    # '''create variable print_myresult and equate it to an empty string where the data will be displayed.
    # Dataretrival process from the database'''
    # print_myresult = " "
    #
    # # creation of a for loop to loop the query
    # for results in myresult:
    #     print_myresult += str(results) +"\n"
    # # printing output from our database
    # print(print_myresult)

    #  Closing the cursor and database after execution.
    mycursor.close()
    my_database.close()

    root.mainloop()


# Creating a function to which is binded to update button

def edit_func():
    # Making edit function global to be used outside the function.
    global edit_func
    # Defining an edit_func window to facilitate
    top = tk.Toplevel(root)
    # Defining the geometry of functions.
    top.geometry("500x500")
    # Defining the title of the edit_func which will display data to be edited
    top.title(" Editing Database")

    # Making variables global to be used outside the function
    global firstname_entry
    global lastname_entry
    global email_entry
    global phonenumber_entry
    global street_address_entry
    global city_entry
    global state_entry
    global zip_code_entry

    # creating labels for the edit-func window page
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

    # creating entry boxes for edit_func which will display the retrieved information.
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
    updatebutton = tk.Button(top, text="Update", command=update_func)
    updatebutton.grid(row=8, column=1)

    # connecting to an existing database to store information which is being input by the user:
    my_database = mysql.connector.connect(
        # location of the database
        host="localhost",
        # defining the user of the database
        user="root",
        # password for mysql workbench to access my database
        password='Kapsabet',
        # higligthing the port of the database
        port="3306",
        # defining or stating the database which all the table which will be used in the project
        database="Workingwithpython"
    )

    # creation of cursor which allows us to send command to database  to do something.
    mycursor = my_database.cursor()
    # Creating a get button to be used to update button
    myrecord = value_button.get()
    # using a cursor to retrieve data which has been saved into database to be updated
    mycursor.execute(" SELECT * FROM personal_information where Personal_id = " + myrecord)

    # allows fetching from the database
    my_data = mycursor.fetchall()

    # looping through the my_data to facilitate retrivial of individual subset
    for record in my_data:
        firstname_entry.insert(0, record[1])
        lastname_entry.insert(0, record[2])
        email_entry.insert(0, record[3])
        phonenumber_entry.insert(0, record[4])
        street_address_entry.insert(0, record[5])
        city_entry.insert(0, record[6])
        state_entry.insert(0, record[7])
        zip_code_entry.insert(0, record[8])

    # creation of a commit to changes we are making to a database.
    my_database.commit()

    # closing the  connection upon completing using the database.
    my_database.close()

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
edit_button = tk.Button(root, text="Edit", command=edit_func)
edit_button.grid(row=10, column=1, padx=10, pady=3, ipadx=50)

# Creating a button to edit has already been input into a database.
delete_button = tk.Button(text="Delete", command="")
delete_button.grid(row=11, column=1, padx=10, pady=5, ipadx=50)

# Creating a button to show button to display what is in the database
show_button = tk.Button(root, text="Show", command=show_value)
show_button.grid(row=12, column=1, padx=10, pady=5, ipadx=50)

root.mainloop()
