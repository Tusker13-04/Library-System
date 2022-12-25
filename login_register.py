# login or register cli
# the encrypted login detais are stored in login mysql table
import sqlalchemy as sq
import getpass
import pandas as pd

con = sq.create_engine('mysql+mysqlconnector://root:Pass@localhost/class_12')
con.connect()
# create a table in  sqlalchemy

df = pd.DataFrame({"username": ["admin"], "password": ["admin"]})
df.to_sql("login", con, if_exists="append", index=False)


def login():
    user = input("Enter your username: ")
    password = input("Enter your password: ")
    query = "SELECT * FROM login WHERE username = '{}' AND password = '{}'".format(user, password)
    result = con.execute(query)
    if result.rowcount == 1:
        print("Login successful")
        import mainpage
        mainpage.main()

    else:
        print("Login failed")


def register():
    user = input("Enter your username: ")
    password = input("Enter your password: ")
    query = "INSERT INTO login (username, password) VALUES ('{}', '{}')".format(user, password)
    result = con.execute(query)
    print("Registration successful")
    main()


def main():
    print("=" * 20, "Login or Register", "=" * 20)
    print()
    print("1. Login")
    print("2. Register")
    print()
    print("=" * 59)

    choice = input("Enter your choice: ")
    if choice == "1":
        login()
    elif choice == "2":
        register()
    else:
        print("Invalid choice")


main()
