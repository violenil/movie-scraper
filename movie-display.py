import csv

myData = { "Once Upon a Time in Hollywood" : { "director" : "Quintin Tarantino", 
            "stars" : ["Leonardo di Caprio", "Brad Pitt", "Margot Robbie", "Emilie Hirsch", "Margaret Quallie", "Timothy Olyphant", "Austin Butler", "Dakota Fanning", "Bruce Dern", "Al Pacino"], 
            "releaseDate" : ["2019-05-21 (Cannes)", "2019-07-26 (United States)", "2019-08-14 (United Kingdom)"], 
            "plot" : "In February 1969, veteran Hollywood actor Rick Dalton, star of 1950s Western television series Bounty Law, fears his career is coming to an end. Casting agent Marvin Schwarz advises him to travel to Italy to make Spaghetti Westerns, which Dalton feels are beneath him. Dalton's best friend and stunt double, Cliff Booth —– a war veteran skilled in hand-to-hand combat[10] who lives in a tiny trailer with his pit bull, Brandy —– drives Dalton around Los Angeles because Dalton's drinking has resulted in several DUI tickets. Booth struggles to find stunt work in Hollywood due to rumors that he murdered his wife. Actress Sharon Tate and her husband, director Roman Polanski, have moved next door to Dalton, who dreams of befriending them as a means of reviving his declining acting career. That night, Tate and Polanski attend a celebrity-filled party at the Playboy Mansion.\n\nThe next day while repairing Dalton's TV antenna, Booth reminisces about a sparring contest he had with Bruce Lee on the set of The Green Hornet which resulted in Booth being fired. Meanwhile, Charles Manson stops by the Polanski residence looking for music producer Terry Melcher, who used to live there, but is turned away by Jay Sebring. Tate goes for errands and stops at a movie theater to watch herself in the film The Wrecking Crew." } }

def displayMovies():
    """
    This is the function that will all you to input queries to the database and all it will do is retrieve the info and print it.
    """
    print("Please select one of the following options to query the database of movies.\n" \
    "(1) Search for a movie in our database.\n" \
    "(2) Display all movie names in alphabetical order.\n" \
    "(3) Display all movie names for given release date.")
    userNeed = input("I want to: ")

def playGame():
    """
    This is the function that has a list of questions for the user and will pick one at random. For each question, an answer is retieved from the database and checked
    against the user input. Should say whether matches or not.
    """


while True:
    modeString = input("Enter 1 for display mode. Enter 2 for game mode. Enter 'q' to exit.\n")

    if modeString == "1":
        print("Display start.")
        displayMovies()
    elif modeString == "2":
        print("Game start.")
        playGame()
    elif modeString == "q":
        break
    else:
        print("Invalid option. Try again.")
