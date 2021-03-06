import csv
import re
import random
from random import seed
from random import randint

myData = { "Once Upon a Time in Hollywood" : { "director" : "Quintin Tarantino", 
            "stars" : ["Leonardo di Caprio", "Brad Pitt", "Margot Robbie", "Emilie Hirsch", "Margaret Quallie", "Timothy Olyphant", "Austin Butler", "Dakota Fanning", "Bruce Dern", "Al Pacino"], 
            "releaseDate" : ["2019-05-21 (Cannes)", "2019-07-26 (United States)", "2019-08-14 (United Kingdom)"], 
            "plot" : "In February 1969, veteran Hollywood actor Rick Dalton, star of 1950s Western television series Bounty Law, fears his career is coming to an end. Casting agent Marvin Schwarz advises him to travel to Italy to make Spaghetti Westerns, which Dalton feels are beneath him. Dalton's best friend and stunt double, Cliff Booth —– a war veteran skilled in hand-to-hand combat[10] who lives in a tiny trailer with his pit bull, Brandy —– drives Dalton around Los Angeles because Dalton's drinking has resulted in several DUI tickets. Booth struggles to find stunt work in Hollywood due to rumors that he murdered his wife. Actress Sharon Tate and her husband, director Roman Polanski, have moved next door to Dalton, who dreams of befriending them as a means of reviving his declining acting career. That night, Tate and Polanski attend a celebrity-filled party at the Playboy Mansion.\n\nThe next day while repairing Dalton's TV antenna, Booth reminisces about a sparring contest he had with Bruce Lee on the set of The Green Hornet which resulted in Booth being fired. Meanwhile, Charles Manson stops by the Polanski residence looking for music producer Terry Melcher, who used to live there, but is turned away by Jay Sebring. Tate goes for errands and stops at a movie theater to watch herself in the film The Wrecking Crew." },
            "Summertime" : { "director" : "Catherine Corsini", 
            "stars" : ["Cecile de France", "Izia Higelin", "Noemie Lvovsky"], 
            "releaseDate" : ["2015-08-06 (Locarno)", "2015-08-19"], 
            "plot" : "Set in 1971, Delphine is the only child of French farmers and enjoys working the land. Though her father wants her to marry, Delphine is secretly pursuing a relationship with a local girl. When she goes for a rendezvous with her, her girlfriend tells her that she plans to marry, dismissing the relationship between her and Delphine as 'not serious': Delphine responds by running away to Paris.\nWalking down a street, Delphine encounters a group of women running by and pinching men's buttocks. When one of the men attacks one of the woman, Delphine helps protect her and learns that her name is Carole. The women belong to a feminist group. which they encourage Delphine to join and participate in their protests. When one of the group members learns that her best friend, a gay man, has been committed to a mental institution by his family and is being given electroshock therapy, the rest of the group refuses at first to help rescue him. Delphine convinces them otherwise, and she, Carole and some of the other women free him. The following night, Delphine kisses Carole, who is surprised and rejects her. The next day Carole tells Delphine that she is not a lesbian, but the two wind up in a passionate embrace. Carole initially believes that it is a one night stand, but quickly develops feelings for Delphine. She tells her boyfriend and the two struggle to work out their relationship even as Carole continues to see Delphine." } }

def movieSearch():
    movieNameList = list(myData.keys())
    while True:
        movieName = input("What movie would you like to search for: ")
        if movieName in movieNameList:
            displayInfo = input("We found it! What would you like to see?\n1) All info\n2) Release date(s)\n3) Director\n4) Stars\n5) Plot\n")
            if displayInfo == "1":
                print(myData[movieName])
            elif displayInfo == "2":
                print(myData[movieName]["releaseDate"])
            elif displayInfo == "3":
                print(myData[movieName]["director"])
            elif displayInfo == "4":
                print(myData[movieName]["stars"])
            elif displayInfo == "5":
                print(myData[movieName]["plot"])
            elif displayInfo == 'q':
                break
            else: print("That's not a valid option. (enter q to exit)")
        elif movieName == 'q':
            break
        else:
            displayInfo = input("That's not a valid option. Try again or enter q to exit")

def cleanDates(dateList):
    newList = []
    for d in dateList:
        newDate = re.sub('-\d{2}-\d{2} \(.*\)$', '', d)
        newList.append(newDate)
    return(newList)

def displayMovies():
    """
    This is the function that will allow you to input queries to the database and all it will do is retrieve the info and print it.
    """
    print("Please select one of the following options to query the database of movies.\n" \
    "(1) Search for a movie in our database.\n" \
    "(2) Display all movie names in alphabetical order.\n" \
    "(3) Display all movie names for given release date.")
    userNeed = input("I want to: ")

    if userNeed == "1":
        movieSearch()

    elif userNeed == "2":
        movieNameList = list(myData.keys())
        movieNameList.sort()
        for m in movieNameList:
            print(m)

    elif userNeed == "3":
        year = input("Please enter the year for which you would like to see all movie titles (only 2015 to 2019): ")
        for movieName, info in myData.items():
            dates = cleanDates(info["releaseDate"])
            if year in dates:
                print(movieName)
            
        
    #else: break

def playGame():
    """
    This is the function that has a list of questions for the user and will pick one at random. For each question, an answer is retieved from the database and checked
    against the user input. Should say whether matches or not.
    """
    print("Here's how the game works. A question is selected at random for you about the movies in our collection ranging from the year 2015 to 2019. You have\n" \
    "three tries to give the correct answer. Upon the third incorrect answer, the correct answer will be revealed. Enter q at any point to quit.\n")
    userQuit = None
    questions = ["Here's a plot. Guess what movie it is from by entering the movie title.", "Here's a movie title. Please name the director of this movie.", 
            "Here's the name of a star. Name one movie he/she acted in between the years 2015 - 2019.", "Here's a movie title. Please name one actor in this movie.",
            "Here's a year. Name one movie that was released that year."]
    while userQuit == None:
        seed(1)
        qVal = randint(0, 4)
       # qVal = 0
        print(questions[qVal] + "\n")
        movie, info = random.choice(list(myData.items()))
        if qVal == 0:
            print(info["plot"] + "\n")
            correctAns = movie
        elif qVal == 1:
            print(movie)
            answer = input("Answer: ")
            correctAns = info["director"]
        elif qVal == 2:
            print(random.choice(info["stars"]))
            answer = input("Answer: ")
            correctAns = movie
        elif qVal == 3:
            print(movie)
            answer = input("Answer: ")
            correctList = info["stars"]
        elif qVal == 4:
            years = ["2015", "2016", "2017", "2018", "2019"]
            chosenYear = random.choice(years)
            print(chosenYear)
            answer = input("Answer: ")
            correctList = list(myData.values())

# this for loop runs every time the while loop iterates (new question)
        
        userAns = input("Answer: ")
        for tries in range(3):
            if userAns == correctAns or userAns in correctList:
                print("Correct!\n")
                break
            elif tries == 2:
                print("Sorry, you're out of tries.\n")
            elif userAns == 'q':
                break
            else:
                print("Incorrect.Try again.\n")
                userAns = input("Answer: ")
        if userAns == "q":
            userQuit = True
print('''
 

 o                   o
    \               __/
     \___          /
         \__    __/
            \  /
 ____________\/____________
/   ____________________   \ 
|  /__/  \__   \__/  \__\  |
| |    __   \__    __   \| |
| |\__/  \__   \__/  \__ | |
| |    __   \__    __   \| |
| |\__/  \__   \__/  \__ | |
| |    __   \__    __   \| |
| |\__/  \__   \__/  \__ | |
| |    __   \__    __   \| |
| |\__/  \__   \__/  \__ | |
|  \________\___________/  |
|                 _   _    |
|  prs           (|) (/)   |
\_________________________/
    "--"           "--"

 _  _   __   _  _  __  ____    ____   __   ____  ____ 
( \/ ) /  \ / )( \(  )(  __)  (  _ \ / _\ / ___)(  __)
/ \/ \(  O )\ \/ / )(  ) _)    ) _ (/    \\___ \ ) _) 
\_)(_/ \__/  \__/ (__)(____)  (____/\_/\_/(____/(____)

        ''')

while True:
    modeString = input("Enter 1 for display mode. Enter 2 for game mode. Enter 'q' to exit.\n")

    if modeString == "1":
        print('''

 ____  __  ____  ____  __     __   _  _    _  _   __  ____  ____ 
(    \(  )/ ___)(  _ \(  )   / _\ ( \/ )  ( \/ ) /  \(    \(  __)
 ) D ( )( \___ \ ) __// (_/\/    \ )  /   / \/ \(  O )) D ( ) _) 
(____/(__)(____/(__)  \____/\_/\_/(__/    \_)(_/ \__/(____/(____)

                ''')
        displayMovies()
    elif modeString == "2":
        print('''

  ___   __   _  _  ____    ____  ____  __   ____  ____ 
 / __) / _\ ( \/ )(  __)  / ___)(_  _)/ _\ (  _ \(_  _)
( (_ \/    \/ \/ \ ) _)   \___ \  )( /    \ )   /  )(  
 \___/\_/\_/\_)(_/(____)  (____/ (__)\_/\_/(__\_) (__)
                                                      
                                                      
                ''')
        playGame()
    elif modeString == "q":
        break
    else:
        print("Invalid option. Try again.")
