import pandas as pd
import mysql.connector as ms
# from database import get_database
import sqlalchemy as sq

global cursor
con = sq.create_engine('mysql+mysqlconnector://root:Pass@localhost/class_12')
connection = con.raw_connection()
cursor = connection.cursor()
global df
# if bookrev table exists in database then pass else create table
try:
    cursor.execute("SELECT * FROM bookrev")

    df = pd.read_sql_query('select * from bookrev', con=con)
except:
    d = {'sno': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
         'book': ["Tale of two cities", "Sense and Sensiblity", "Journey to the end of the Earth",
                  "The Count of Monte Cristo", "Romeo and Juliet", "One Arranged Murder", "Twilight", "IT",
                  "Pride and Prejudice", "The fault in our stars", "The Bourne Identity", "My Man Jeeves",
                  "Harry Potter", "The Bourne Ultimatum", "The Bourne Supremacy", "Ponniyin Selvan"],
         'author': ["Charles Dickens", "Jane Austen", "Jules Verne", "Alexandre Dumas", "William Shakespeare",
                    "Chetan Bhagat", "Stephanie Meyer", "Stephen King", "Jane Austen", "John Green", "Robert Ludlum",
                    "PG Woodhouse", "J.K.Rowling", "Robert Ludlum", "Robert Ludlum", "Kalki Krishnamurthy"],
         'rating': [3.86, 4.1, 4, 4.28, 3.35, 3.5, 3.63, 4.6, 4.28, 4.26, 4.04, 4.07, 3.85, 4.06, 4, 4.98],
         'genre': ["fiction", "period drama", "adventure", "adventure", "romance", "mystery", "sci-fiction", "horror",
                   "romance", "romance", "action-thriller", "comedy", "fictional", "action-thriller", "action-thriller",
                   "drama"],
         'review': [
             "Profound human love and the most repugnant savagery , horror and redemption, a heroine and a grotesque revenger, two families with dark secrets, two cities, all in the backdrop of the bloodbath that was the French Revelation. In reading it, be prepared for the Best of Times and the Worst of Times. Like all great stories, the brilliance of this tale is its ability to not only intimately draw us into the tangled lives of these characters, battered by the historical tyrannies of their time, but to use their story as a parable to understand the human narrative. Perhaps therefore Dickens believed this book to be his magnum opus; perhaps he felt like it was his clearest statement of what he believed.",
             "When Elinor Dashwoods father dies, her family\'s finances are crippled. After the Dashwoods move to a cottage in Devonshire, Elinors sister Marianne is torn between the handsome John Willoughby and the older Colonel Brandon. Meanwhile, Elinors romantic hopes with Edward Ferrars are hindered due to his prior engagement. Both Elinor and Marianne strive for love while the circumstances in their lives constantly change",
             "This novel, instead of going around the world, we are now going into it! Though most adventures and action books these days rely on shoot outs and car chases to keep the reader interested, Jules Verne manages to grip us using old fashioned mystery and suspense. The epic adventure begins when enthusiastic geologist Professor Otto Liedenbrock discovers old documents, which he believes are instructions on getting to the centre of the earth. Along with his whiz-kid nephew, Axel Liedenbrock he discovers the key to the document, and finds the location of the crater. They pack any and every survival equipment they can find, but will it be enough for the perilous journey ahead? Will their supplies last? How will they get back up to the surface? Will they ever get back up to the surface? They must find their way through a maze and an endless sea, as well as many other obstacles before they can find their way to the heart of the earth.",
             "Thrown in prison for a crime he has not committed, Edmond Dant\'es is confined to the grim fortress of If. There he learns of a great hoard of treasure hidden on the Isle of Monte Cristo and he becomes determined not only to escape, but also to unearth the treasure and use it to plot the destruction of the three men responsible for his incarceration. Dumas\'92 epic tale of suffering and retribution, inspired by a real-life case of wrongful imprisonment, was a huge popular success when it was first serialized in the 1840sRobin Buss\'92s lively English translation is complete and unabridged, and remains faithful to the style of Dumas\'92s original. This edition includes an introduction, explanatory notes, and suggestions for further reading.",
             "It is well known that Shakespeare borrowed plot ideas liberally from ancient Greek plays. However, with Romeo and Juliet, he broke new ground. Of course, it wasn’t the first tragedy but it was the first to use love as the hero’s fatal flaw. The impact of this has shaped culture immeasurably. It is such a good story. It truly is timeless and has been borrowed and liberally ripped off for centuries since.",
             "The book follows two best friends who have a detective agency. Keshav and Saurabh live together, work together and are close, despite their differences. Saurabh is to marry Prerna, and though its an arranged marriage they seem very much in love. Even though theyre just engaged she fasts for him on Karva Chauth and insists on meeting him on the terrace so that she can eat.Unfortunately Saurabh reaches the terrace to find her murdered. He is determined to find the killer so he and Keshav investigate together. Prerna lived in a big house in Delhi and there are a lot of suspects.The book is written in Bhagats signature easy style and those who have read the timeless romances by Bhagat will be thrilled reading this new genre.",
             "Twilight is an interesting, mysterious portal into a riveting take on traditional vampires and delves into how a more realistic yet more fantastical type of vampire could exist among us. It draws you in with the mystery of Edward, making you wonder what his deal is. You are kept engaged by the relatable (and not so relatable) struggles of Bella, an everyday girl who has just moved to a new school and is drawn to a mysterious, beautiful boy named Edward. She continually gets into awkward situations that she would not be able to get herself out of, if it wasnt for Edward. What is Edwards goal? Why is she so attracted to him? And why does he force her away repeatedly? Read to find out!",
             "\'It\' is a book that sticks to your mind as a reader. Readers will find themselves entangled in the fictional world Stephen King created, and one will experience the emanating horror from a personal perspective. In all honest opinion, though the book is lengthy, reading It is worth all the pages",
             "Pride and Prejudice Book Review Pride and Prejudice, a classic novel by Jane Austen, tells the story of a complicated love that develops between what was thought to be two very different personalities. The protagonist, Elizabeth Bennet, misjudges a man upon rumor and appearance, but finds out she is extraordinarily wrong.",
             "The Fault in Our Stars is a great novel. The characters, dialogues, and themes work perfectly in sync to create a story that draws out emotions from the reader. Because it pays attention to the lives of its characters intricately, the novel makes the reader relate to the story personally. The Fault in Our Stars employed an excellent writing technique that disseminated story plots progressively. The use of compact sentences with a detailed description of events made the story leave an impression of realism on the mind of its reader. John Greens use of simple wording made the story compact.",
             "A gripping, edge of the seat thriller from a master storyteller, \'The Bourne Identity\' sets the standard for an engrossing action adventure against which other books will shoot in vain!Who is Jason Bourne? Is he an assassin, a terrorist, a thief? Why has he got four million dollars in a Swiss bank account ? Why has someone tried to murder him? ... Jason Bourne does not know the answer to any of these questions. Suffering from amnesia, he does not even know that he is Jason Bourne. What manner of man is he? What are his secrets? Who has he killed?",
             "Stories of rich men being nice to their fellow rich friends, or deceiving their rich families, are everywhere. That there is an inherent goodness in Wooster (or his doppelganger, Pepper--Wodehouse switches protagonists & they are pretty identical other than by name, which is indeed part of the theme that all aristocrats are equally dim) may be the takeaway here, in these modern times. Jeeves is the perpetual Everyman, trapped in a world hes too good for, being appreciated & always adulated by the Gods; remaining in that constant position, always in some unworthy persons life (tragically so).",
             "Harry Potter was given a scar by Voldemort the night his parents sacrificed themselves. And from that night onwards, he was no longer an ordinary boy but the Boy who lived. When Harry turns 11, he receives a letter from Hogwarts, a school for witchcraft and magic. He is very excited to go there and escape his cruel aunt and uncle. And soon, Hogwarts becomes his home, a place where he could be himself, explore his capabilities, make new friends, and find happiness. But this happiness is short-lived, as Voldemort wants to finish what he had started eleven years ago-to kill Harry. However, his friends will not let this happen. They are there to support him and protect him. And so begins the journey of Harry, from learning wizardry to excelling in Quidditch, making friends, finding love, and even flying cars!",
             "Now David Webb, professor of Oriental studies, husband, and father, must do what he hoped he would never have to do again: assume the terrible identity of Jason Bourne. His plan is simple: to infiltrate the politically and economically Medusan group and use himself as bait to lure the cunning Jackal into a deadly trap, a trap from which only one of them will escape themselves.",
             "The Bourne Supremacy is a smooth thriller for grown-ups with lots of chase scenes and action scenes, but the mood is dark, even grim. The dialogue is smart but not smart-alecky. Instead of flashy fights where one dazzling kick to the throat knocks the bad guy out, the battles are messy and breathless and brutal.",
             "There’s the brilliant storytelling, that makes even this long novel that spans 500 chapters, 2,400 pages, an un-put-downable book. The tense verbal fencing and pithy dialogue that sparkles and shines in every conversation.The never-ending cast with their unique personalities and characters – some noble, others dastardly, some ferocious, others cunning, some foolhardy, others ruthless. And there is the use of so many literary devices that make it an intriguing, gripping read. Cliff-hangers end each chapter. Emotions surge and swell as opponents pit wits and weapons, strategize, and conspire against each other."]}

    df = pd.DataFrame(d)

    df.to_sql(name="bookrev", if_exists="append", con=con, index=False)
    print("Data written to SQL")


# adding records to the csv file
def adding():
    # adding new books
    numOfEntry = int(input("Enter the number of books you want to add: "))
    for i in range(numOfEntry):
        global df

        # auto increment book id
        BookID = len(df) + 1
        BookName = input('Enter the Book Name: ')
        Author = input('Enter the Author Name: ')
        Rating = input('Enter the Rating: ')
        Genre = input('Enter the Genre: ')
        Review = input('Enter the Review: ')

        d = {'sno': BookID, 'book': BookName, 'author': Author, 'rating': Rating, 'genre': Genre, 'review': Review}
        new = pd.DataFrame(d, index=[0])

        if BookName.lower() in df['book'].str.lower().values:
            print("Book already present")
            continue
        else:
            df = pd.concat([df, new], ignore_index=True)
            new.to_sql('bookrev', con=con, if_exists="append", index=False)

        # print sql table
        print(pd.read_sql_query('select * from bookrev', con=con))
    main()


# reading a review
def ask():
    # return review by sno
    ask = input("Enter the serial number of book to read the review: ")

    print(pd.read_sql_query("SELECT review FROM bookrev WHERE sno = %s", con, params=(ask,)))

    main()


def reading():
    print(df["book"])

    # reading a review from sql bookrev table by book name
    book_name = input("Enter the book name: ")
    # check if the book name exists in the df
    if book_name.lower() in df['book'].str.lower().values:
        # print review from sql
        cursor.execute("SELECT review FROM bookrev WHERE book = %s", (book_name,))

        print(pd.DataFrame(cursor.fetchall()))
        # show full review

    else:
        print("Book not found")
    main()


def author():
    print(df["author"])
    # reading a review by the authors name
    author_name = input("Enter the author name: ")
    # check if the author name exists in the df
    if author_name.lower() in df['author'].str.lower().values:
        # print review from sql
        print(pd.read_sql_query("SELECT book,review FROM bookrev WHERE author = %s", con, params=(author_name,)))
    else:
        print("Author not found")
    main()


# reading review by genre
def genre():
    print(df["genre"].unique())
    # reading review by genre
    genre_name = input("Enter the genre name: ")
    # check if the genre name exists in the df
    if genre_name.lower() in df['genre'].str.lower().values:
        # print review from sql
        print(pd.read_sql_query("SELECT book,review FROM bookrev WHERE genre = %s", con, params=(genre_name,)))
    else:
        print("Genre not found")
    main()


def topten():
    # displaying the top ten books with the highest rating from sql
    print(pd.read_sql_query("SELECT sno,book,rating FROM bookrev ORDER BY rating DESC LIMIT 5", con))

    yorn = input("Do you want to read a review of any book?(yes/no): ")

    if yorn.lower() == 'yes':
        ask()

    else:
        print("Thank you.")
        main()


def main():
    print('''
 
    ====================| WELCOME TO SNS BOOKREVZZ |=====================
                        1. READ A REVIEW BY THE BOOK NAME.
                        2. READ A REVIEW BY THE AUTHOR NAME.
                        3. READ A REVIEW BY GENRE
                        4. WRITE A REVIEW.
                        5. THE TOP TEN BOOKS.
                        6. EXIT
        
    ''')

    choice = int(input("YOUR CHOICE?(1/2/3/4/5/6/7) "))

    if choice == 1:
        reading()

    elif choice == 2:
        author()

    elif choice == 3:
        genre()

    elif choice == 4:
        adding()

    elif choice == 5:
        topten()

    else:
        print("Thank you for visiting! Hope to better our services next time :D")


main()
