"""
Deal with Nan in json.
check if choose_right_question works.
"""
import json
import random
import re


def movieSearch(content):
    movieNList = []
    for item in content:
        movieName = item['Movie_name']
        movieNList.append(movieName)
    movieNameList = cleanNames(movieNList)

    while True:
        movieName = input("What movie would you like to search for: ")
        if movieName in movieNameList:
            displayInfo = input("We found it! What would you like to see?\n1) All info\n2) Release date(s)\n3) Director\n4) Stars\n5) Plot\n")
            for m in content:
                if m['Movie_name'] == movieName:
                    movieContent = m

            if displayInfo == "1":
                print(movieContent)   #to print everything
            elif displayInfo == "2":
                print(movieContent['Release_dates'])  #prints only release dates
            elif displayInfo == "3":
                print(movieContent["Director"])  #prints only director
            elif displayInfo == "4":
                print(movieContent["Characters"])
            elif displayInfo == "5":
                print(movieContent["Plot"])
        elif movieName == 'q':
            break
        else:
            print("Sorry, we did'nt find this movie. Try again or enter 'q' to exit")

def cleanNames(nameList):
    newList = []
    for n in nameList:
        newName = re.sub(' \(.*\)$', '', n)
        newList.append(newName)
    return(newList)

def cleanDates(dateList):
    newList = []
    for d in dateList:
        name = d[1:]
        newDate = name[:4]
        newList.append(newDate)
    return(newList)

def displayMovies(content):
    """
    This is the function that will allow you to input queries to the database and all it will do is retrieve the info and print it.
    """
    print("Please select one of the following options to query the database of movies. Press 'q' to exit.\n" \
    "(1) Search for a movie in our database.\n" \
    "(2) Display all movie names in alphabetical order.\n" \
    "(3) Display all movie names for given release date.")
    userNeed = input("I want to: ")

# Just compiling a list of Movie Names here quick
    movieNList = []
    for item in content:
        movieName = item['Movie_name']
        movieNList.append(movieName)
    movieNameList = cleanNames(movieNList) #some movies have format 'MovieName (2019 film)' --> want to only get name
    
    if userNeed == "1":
        movieSearch(content)
    elif userNeed == "2":
        movieNameList.sort()
        for m in movieNameList:
            print(m)
    elif userNeed == "3":
        year = input("Please enter the year for which you would like to see all movie titles (only 2015 to 2019): ")
        for m in content:
            dates = cleanDates(m['Release_dates'])
            if year in dates:
                print(m['Movie_name'])
        print('')
    #else: break


def ask_movie_name(pick):
    print(pick['Plot'])
    q = ('This Plot belongs to which movie?')
    return q, pick['Movie_name']


def ask_director(pick):
    print(pick['Movie_name'])
    q = ('Who is the Director this movie?')
    return q, pick['Director']


def ask_movie_name_given_characters(pick):
    q = (','.join(pick['Characters']), 'Which movie did these stars play in?')
    return q, pick['Movie_name']


def ask_characters(pick):
    print(pick['Movie_name'])
    q = ('Who acted in this movie?')
    return q, pick['Characters']


def ask_release_date(pick):
    print(pick['Movie_name'])
    q = ('What is the release date of this movie?')
    dates = cleanDates(pick['Release_dates'])
    return q, dates 

def choose_right_question(pick):
    """
    we do not choose the option of printing the plot and asking questions based on that if plot == nan.
    we do not chooce the option of printing the characters if tere is "No Star" in list of characters.
    """
    if not pick['Plot'] and pick['Characters']==['No stars']:
        question= random.choice([2,4,5])
        return question
    elif not pick['Plot']:
        question =random.choice([2,3,4,5])
        return question
    elif pick['Characters']==['No stars']:
        question = random.choice([1, 2, 4, 5])
        return question
    else:
        question= random.choice([1,2,3,4,5])
        return question

def playGame(content):   
    print("Here's how the game works. A question is selected at random for you about the movies in our collection ranging from the year 2015 to 2019. You have\n" \
    "three tries to give the correct answer. Upon the third incorrect answer, the correct answer will be revealed. Enter q at any point to quit.\n")
    userQuit = None
    while userQuit == None:
        pick = random.choice(content)
        question= choose_right_question(pick)
        
        if question == 1:
            q, a = ask_movie_name(pick)
        if question == 2:
            q, a = ask_director(pick)
        if question == 3:
            q, a = ask_movie_name_given_characters(pick)
        if question == 4:
            q, a = ask_characters(pick)
        if question == 5:
            q, a = ask_release_date(pick)

        print(q)
        correct = False
        chance = 3

        user_answer = input()
        if user_answer == 'q': break

        while not correct and chance > 1:
            chance -= 1
            if type(a) == list:
                for i in a:
                    if i == user_answer:
                        print("*** You are correct ***")
                        correct=True
                        break
                if not correct:
                    print("You said {} which is wrong. You have {} tries.".format(
                    user_answer, chance))
                    user_answer = input()
            elif user_answer == a:
                print("*** You are correct ***")
                correct = True
            else:
                print("You said {} which is wrong you have {} tries".format(
                    user_answer, chance))
                user_answer = input()
                if user_answer == 'q': break

        if not correct:
            print("\n\t ** The correct answer is {}".format(a))



if __name__ == "__main__":
    f = open('movie_json.json', 'r')
    content = json.load(f)
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
            displayMovies(content)
        elif modeString == "2":
            print('''

  ___   __   _  _  ____    ____  ____  __   ____  ____
 / __) / _\ ( \/ )(  __)  / ___)(_  _)/ _\ (  _ \(_  _)
( (_ \/    \/ \/ \ ) _)   \___ \  )( /    \ )   /  )(
 \___/\_/\_/\_)(_/(____)  (____/ (__)\_/\_/(__\_) (__)


                ''')
            playGame(content)
        elif modeString == "q":
            break
        else:
            print("Invalid option. Try again.")
