import csv
from prettytable import PrettyTable

# creating a data file

details = ['S.NO', 'book', 'author', 'rating', 'genre', 'review']

rows = [[1, 'Tale of two cities', 'Charles Dickens', 3.86, 'fiction',
         'Profound human love and the most repugnant savagery, horror and redemption, a heroine and a grotesque revenger, two families with dark secrets, two cities, all in the backdrop of the bloodbath that was the French Revelation. In reading it, be prepared for the Best of Times and the Worst of Times. Like all great stories, the brilliance of this tale is its ability to not only intimately draw us into the tangled lives of these characters, battered by the historical tyrannies of their time, but to use their story as a parable to understand the human narrative. Perhaps therefore Dickens believed this book to be his magnum opus; perhaps he felt like it was his clearest statement of what he believed.'],
        [2, 'Sense and Sensiblity', 'Jane Austen', 4.1, 'period drama',
         'When Elinor Dashwoods father dies, her familys finances are crippled. After the Dashwoods move to a cottage in Devonshire, Elinors sister Marianne is torn between the handsome John Willoughby and the older Colonel Brandon. Meanwhile, Elinors romantic hopes with Edward Ferrars are hindered due to his prior engagement. Both Elinor and Marianne strive for love while the circumstances in their lives constantly change'],
        [3, 'Journey to the end of the Earth', 'Jules Verne', 4.0, 'adventure',
         'This novel, instead of going around the world, we are now going into it! Though most adventures and action books these days rely on shoot outs and car chases to keep the reader interested, Jules Verne manages to grip us using old fashioned mystery and suspense. The epic adventure begins when enthusiastic geologist Professor Otto Liedenbrock discovers old documents, which he believes are instructions on getting to the centre of the earth. Along with his whiz-kid nephew, Axel Liedenbrock he discovers the key to the document, and finds the location of the crater. They pack any and every survival equipment they can find, but will it be enough for the perilous journey ahead? Will their supplies last? How will they get back up to the surface? Will they ever get back up to the surface? They must find their way through a maze and an endless sea, as well as many other obstacles before they can find their way to the heart of the earth.'],
        [4, 'The Count of Monte Cristo', 'Alexandre Dumas', 4.28, 'adventure',
         'Thrown in prison for a crime he has not committed, Edmond Dant\'es is confined to the grim fortress of If. There he learns of a great hoard of treasure hidden on the Isle of Monte Cristo and he becomes determined not only to escape, but also to unearth the treasure and use it to plot the destruction of the three men responsible for his incarceration. Dumas\'92 epic tale of suffering and retribution, inspired by a real-life case of wrongful imprisonment, was a huge popular success when it was first serialized in the 1840sRobin Buss\'92s lively English translation is complete and unabridged, and remains faithful to the style of Dumas\'92s original. This edition includes an introduction, explanatory notes, and suggestions for further reading.'],
        [5, 'Romeo and Juliet', 'William Shakespeare', 3.35, 'romance',
         'It is well known that Shakespeare borrowed plot ideas liberally from ancient Greek plays. However, with Romeo and Juliet, he broke new ground. Of course, it wasn’t the first tragedy but it was the first to use love as the hero’s fatal flaw. The impact of this has shaped culture immeasurably. It is such a good story. It truly is timeless and has been borrowed and liberally ripped off for centuries since. '],
        [6, 'One Arranged Murder', 'Chetan Bhagat', 3.5, 'mystery',
         'The book follows two best friends who have a detective agency. Keshav and Saurabh live together, work together and are close, despite their differences. Saurabh is to marry Prerna, and though its an arranged marriage they seem very much in love. Even though theyre just engaged she fasts for him on Karva Chauth and insists on meeting him on the terrace so that she can eat.Unfortunately Saurabh reaches the terrace to find her murdered. He is determined to find the killer so he and Keshav investigate together. Prerna lived in a big house in Delhi and there are a lot of suspects.The book is written in Bhagats signature easy style and those who have read the timeless romances by Bhagat will be thrilled reading this new genre.'],
        [7, 'Twilight', 'Stephanie Meyer', 3.63, 'sci-fiction',
         'Twilight is an interesting, mysterious portal into a riveting take on traditional vampires and delves into how a more realistic yet more fantastical type of vampire could exist among us. It draws you in with the mystery of Edward, making you wonder what his deal is. You are kept engaged by the relatable (and not so relatable) struggles of Bella, an everyday girl who has just moved to a new school and is drawn to a mysterious, beautiful boy named Edward. She continually gets into awkward situations that she would not be able to get herself out of, if it wasnt for Edward. What is Edwards goal? Why is she so attracted to him? And why does he force her away repeatedly? Read to find out!'],
        [8, 'IT', 'Stephen King', 4.6, 'horror',
         '‘It’ is a book that sticks to your mind as a reader. Readers will find themselves entangled in the fictional world Stephen King created, and one will experience the emanating horror from a personal perspective. In all honest opinion, though the book is lengthy, reading It is worth all the pages'],
        [9, 'Pride and Prejudice', 'Jane Austen', 4.28, 'romance',
         'Pride and Prejudice Book Review Pride and Prejudice, a classic novel by Jane Austen, tells the story of a complicated love that develops between what was thought to be two very different personalities. The protagonist, Elizabeth Bennet, misjudges a man upon rumor and appearance, but finds out she is extraordinarily wrong.'],
        [10, 'The fault in our stars', 'John Green', 4.26, 'romance',
         'The Fault in Our Stars is a great novel. The characters, dialogues, and themes work perfectly in sync to create a story that draws out emotions from the reader. Because it pays attention to the lives of its characters intricately, the novel makes the reader relate to the story personally. The Fault in Our Stars employed an excellent writing technique that disseminated story plots progressively. The use of compact sentences with a detailed description of events made the story leave an impression of realism on the mind of its reader. John Greens use of simple wording made the story compact.'],
        [11, 'The Bourne Identity', 'Robert Ludlum', 4.04, 'action-thriller',
         'A gripping, edge of the seat thriller from a master storyteller, ‘The Bourne Identity‘ sets the standard for an engrossing action adventure – against which other books will shoot in vain!Who is Jason Bourne? Is he an assassin, a terrorist, a thief? Why has he got four million dollars in a Swiss bank account? Why has someone tried to murder him? ...Jason Bourne does not know the answer to any of these questions. Suffering from amnesia, he does not even know that he is Jason Bourne. What manner of man is he? What are his secrets? Who has he killed?'],
        [12, 'My Man Jeeves', 'PG Woodhouse', 4.07, 'comedy',
         'Stories of rich men being nice to their fellow rich friends, or deceiving their rich families, are everywhere. That there is an inherent goodness in Wooster (or his doppelganger, Pepper--Wodehouse switches protagonists & they are pretty identical other than by name, which is indeed part of the theme that all aristocrats are equally dim) may be the takeaway here, in these modern times. Jeeves is the perpetual Everyman, trapped in a world hes too good for, being appreciated & always adulated by the Gods; remaining in that constant position, always in some unworthy persons life (tragically so).'],
        [13, 'Harry Potter', 'J.K.Rowling', 3.85, 'fictional',
         'Harry Potter was given a scar by Voldemort the night his parents sacrificed themselves. And from that night onwards, he was no longer an ordinary boy but the Boy who lived. When Harry turns 11, he receives a letter from Hogwarts, a school for witchcraft and magic. He is very excited to go there and escape his cruel aunt and uncle. And soon, Hogwarts becomes his home, a place where he could be himself, explore his capabilities, make new friends, and find happiness. But this happiness is short-lived, as Voldemort wants to finish what he had started eleven years ago-to kill Harry. However, his friends will not let this happen. They are there to support him and protect him. And so begins the journey of Harry, from learning wizardry to excelling in Quidditch, making friends, finding love, and even flying cars!'],
        [14, 'The Bourne Ultimatum', 'Robert Ludlum', 4.06, 'action-thriller',
         'Now David Webb, professor of Oriental studies, husband, and father, must do what he hoped he would never have to do again: assume the terrible identity of Jason Bourne. His plan is simple: to infiltrate the politically and economically Medusan group and use himself as bait to lure the cunning Jackal into a deadly trap, a trap from which only one of them will escape themselves.'],
        [15, 'The Bourne Supremacy', 'Robert Ludlum', 4.0, 'action-thriller',
         'The Bourne Supremacy is a smooth thriller for grown-ups with lots of chase scenes and action scenes, but the mood is dark, even grim. The dialogue is smart but not smart-alecky. Instead of flashy fights where one dazzling kick to the throat knocks the bad guy out, the battles are messy and breathless and brutal.'],
        [16, 'Ponniyin Selvan', 'Kalki Krishnamurthy', 4.98, 'drama',
         'There’s the brilliant storytelling, that makes even this long novel that spans 500 chapters, 2,400 pages, an un-put-downable book. The tense verbal fencing and pithy dialogue that sparkles and shines in every conversation.The never-ending cast with their unique personalities and characters – some noble, others dastardly, some ferocious, others cunning, some foolhardy, others ruthless. And there is the use of so many literary devices that make it an intriguing, gripping read. Cliff-hangers end each chapter. Emotions surge and swell as opponents pit wits and weapons, strategize, and conspire against each other.']]

with open("temp/bookrev.csv", 'w', newline='') as f:
    write = csv.writer(f)
    write.writerow(details)
    write.writerows(rows)


# adding records to the csv file
def adding():
    f = open("temp/bookrev.csv", "a")

    n = int(input("Enter the number of books you want to add: "))

    for i in range(n):
        sno = int(input("Enter the sno of the book"))
        book = input("Enter the name of the book: ")
        author = input("Enter the name of the author: ")
        rating = input("Rating of the specified book: ")
        genre = input("Genre of the specified book: ")
        review = input("Review of the specified book: ")
        det = [[sno, book, author, rating, genre, review]]
        # check if book name already exists under column book in csv file ignore case sensitivity
        with open("temp/bookrev.csv", 'r') as f:
            reader = csv.reader(f)
            for row in reader:

                if book.lower() == row[1].lower():
                    print("Book already exists")
                    break

                elif str(sno) == row[0]:
                    print("Serial number already exists")
                    break
            else:

                with open("temp/bookrev.csv", 'a') as f:
                    write = csv.writer(f)
                    write.writerows(det)
                    print("Book added successfully")
                    print("The review has been added successfully! Thank you for your feedback :) ")

    f.close()


# reading a review
def ask():
    aski = input("READ A REVIEW? ENTER THE 'SNO' OF THE BOOK OF YOUR CHOICE: ")
    f = open("temp/bookrev.csv", "r")
    csv_r = csv.reader(f)
    read = list(csv_r)
    for i in read:
        if i == []:
            pass
        elif aski == i[0]:
            print(" ")
            print('REVIEW: ', i[5])
            print(" ")
            print("AUTHOR: ", i[2])
            print(" ")
            print("GENRE: ", i[4])
            print(" ")
            print("RATING: ", i[3])
            print(" ")


def reading():
    f = open("temp/bookrev.csv", "r")
    csv_r = csv.reader(f)
    read = list(csv_r)
    book = input("name of the book :")
    A = []
    for i in read:
        if i == []:
            pass
        for j in i:
            if book.lower() in j.lower():
                a = i[0]
                b = i[1]
                c = i[2]
                A.append([a, b, c])
                table = PrettyTable(['SNO', 'BOOKS', 'author'])
                table.add_rows(A)
                break

    print(table)

    ask()
    f.close()


# reading a review by the authors name
def author():
    f = open("temp/bookrev.csv", "r", newline="")
    read = csv.reader(f)
    L = list(read)
    name_author = input("Enter the name of the author: ")
    A = []
    for i in L:

        if i == []:
            pass

        elif i[2].lower() == name_author.lower():
            b = i[1]
            a = i[0]
            A.append([a, b])
            table = PrettyTable(['SNO', 'BOOKS'])
            table.add_rows(A)

    print(table)
    ask()
    f.close()


# reading review by genre
def genre():
    f = open("temp/bookrev.csv", "r", newline="")
    read = csv.reader(f)
    L = list(read)
    genre = input("Enter the genre of the book: ")
    A = []
    for i in L:

        if i == []:
            pass

        elif i[4].lower() == genre.lower():
            b = i[1]
            a = i[0]
            A.append([a, b])
            table = PrettyTable(['SNO', 'BOOKS'])
            table.add_rows(A)

    print(table)
    ask()
    f.close()


# displaying the top ten books.
def topten():
    f = open("temp/bookrev.csv")
    read = csv.reader(f)
    L = list(read)
    A = []
    for i in L:

        if i == []:
            pass

        else:
            a = i[3]
            b = i[1]
            c = i[2]
            d = i[0]
            A.append([a, b, c, d])

    A.sort(reverse=True)
    l1 = A[1:11]

    for i in range(len(l1)):
        table = PrettyTable(['RATING', 'BOOKNAME', 'AUTHOR', 'SNO'])
        table.add_rows(l1)
    print("            - T O P  T E N  B O O K S - ")
    print(table)
    yorn = input("Do you want to read a review of any book?(yes/no): ")

    if yorn == 'yes':
        ask()

    else:
        print("Thank you.")
    f.close()


while True:

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
        break
