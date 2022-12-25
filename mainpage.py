#welcome cli with opption to rent a book or buy a book or review a book

import pandas as pd
import sqlalchemy as sq
con=sq.create_engine('mysql+mysqlconnector://root:Pass@localhost/class_12')
import datetime as DT
today = DT.date.today()
return_date = today + DT.timedelta(days=7)
connection = con.raw_connection()
cursor = connection.cursor()
try:
    cursor.execute("SELECT * FROM borrowbook")

    df = pd.read_sql_query('select * from borrowbook', con=con)
except:
    df=pd.DataFrame({"book":["Adventures of Tom Sawyer","Alice in Wonderland","Origin of Species"],"author":["Mark Twain","Lewis Carrol","Charles Darwin"],"price":[100,200,150],"status":["available","rent","sold"]})
    df.to_sql("borrowbook",con,if_exists="append",index=False)
def rent_book():
    print("="*50)
    print(pd.read_sql("select * from BorrowBook",con))
    print("="*50)
    rent_book=input("Enter the book you want to rent: ")
    #check if book status is available
    query="select * from BorrowBook where book='{}' and status='available'".format(rent_book)
    result=con.execute(query)
    if result.rowcount==1:
        query="UPDATE BorrowBook SET status='rent' WHERE book='{}'".format(rent_book)
        result=con.execute(query)
        print("You mut return the book ",rent_book,"on" ,return_date)
        print("Thank you for renting the book")
    else:
        print("Book is not available")
    main()
def buy_book():
    print("="*50)
    print(pd.read_sql("select * from BorrowBook",con))
    print("="*50)
    buy_book=input("Enter the book you want to buy: ")
    query="select * from BorrowBook where book='{}' and status='available'".format(buy_book)
    result=con.execute(query)
    if result.rowcount==1:
        purchase=0
        card=input("Enter your card number: ")
        cvv=input("Enter your cvv number: ")
        if len(card)>13 and len(cvv)>2:
            #get fist digit of card number

            first_digit=card[0]

            if first_digit=="4":
                print("Your purchase via visa card has been successful")
                purchase=1
            elif first_digit=="5":
                print("Your purchase via master card has been successful")
                purchase=1
            elif first_digit=="6":
                print("Your purchase via discover card has been successful")
                purchase=1
            else:
                print("Invalid card number")
                purchase=0
        if purchase==1:
            query="UPDATE BorrowBook SET status='sold' WHERE book='{}'".format(buy_book)
            result=con.execute(query)
            print("Thank you for buying the book")

        else:
            print("Book is not available")
    main()

def review_book():
    import LibraryReview
    LibraryReview.main()

def main():
    print("="*20,"Welcome to SNS Library","="*20)
    print("1. Rent a book")
    print("2. Buy a book")
    print("3. Review a book")
    choice=input("Enter your choice: ")
    if choice=="1":
        rent_book()
    elif choice=="2":
        buy_book()
    elif choice=="3":
        review_book()
    else:
        print("Invalid choice")
main()




