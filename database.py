import mysql.connector

mydatabase = mysql.connector.connect(
    host="localhost",
    user="root",
    password='Kapsabet',
    port="3306",
    # database="Workingwithpython"
)

# Creating a cursor object to use in database

mycursor = mydatabase.cursor()

# creating a database
mycursor.execute("CREATE DATABASE Workingwithpython")

# mycursor.execute("SHOW DATABASES")
#
# for database in mycursor:
#     print(database[0])
#
# mycursor.execute("CREATE TABLE IF NOT EXISTS Personal_information("
#                  "Personal_id int auto_increment PRIMARY KEY,"
#                  " Firstname varchar(255) NOT NULL,"
#                  "Lastname varchar(255) NOT NULL, "
#                  "mail varchar(45) NOT NULL,"
#                  " Phonenumber integer NOT NULL,"
#                  "Street_Address varchar(255) NOT NULL,"
#                  "City varchar(255) NOT NULL,"
#                  "State varchar(255)NOT NULL,"
#                  "Zipcode integer(10) NOT NULL) ")
#
# mycursor.execute("SHOW TABLES")
#     for x in mycursor:
#         print(x)

# sql_insertion = ("INSERT INTO Personal_information("
#                  "Firstname,"
#                  " Lastname,"
#                  " mail,"
#                  "Phonenumber,"
#                  "Street_Address,"
#                  "City,"
#                  "State,"
#                  "Zipcode) "
#                  "values (%s,%s,%s,%s,%s,%s,%s,%s)")
# record_values = [("Kip",
#                   "Robert",
#                   "kiprobert@gmail.com",
#                   33339999,
#                   "2112 Cleveland Blvd",
#                   "Caldwell",
#                   "Idaho",
#                   81605),
#                  ("Kiplangat",
#                   "Chumba",
#                   "kiplangat.chumba@gmail.com",
#                   857375272,
#                   "3112 Cleveland Blvd",
#                   "Spokane",
#                   "Washington",
#                   13605),
#                  ("Will",
#                   "Smith",
#                   "Smith.will@gmail.com",
#                   987654321,
#                   "2112 Cleveland Blvd",
#                   "Caldwell",
#                   "Idaho",
#                   83605),
#                  (
#                      "Kiprono",
#                      "Evans",
#                      "Evanskiprono@gmail.com",
#                      123456789,
#                      "2112 West Coast Blvd",
#                      "Caldwell",
#                      "Nebraska",
#                      22205)
#
#
# ]
#
# mycursor.executemany(sql_insertion, record_values)
mydatabase.commit()
mydatabase.close()