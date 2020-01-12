import sys
import requests  # to download
import bs4
import csv
import re

def findMovieName(infoSoup):
    '''
    The simplest of them all.
    '''
    return(infoSoup.tr.string)

def findDirector(infoSoup):
    '''
    Almost as simple as movie name. But directors seem to be stored in 2 different ways.
    '''
    director = ""
    all_tr = infoSoup.find_all('tr')    #saving all table rows to this, can iterate through them
    for tr in all_tr:
        if tr.th != None:
            if tr.th.string == "Directed by":
                director = tr.th.next_sibling.string
        if director == None:
            director = tr.th.next_sibling.get_text()
    return(director)

def findReleaseDate(infoSoup):
    '''
    Dates in html are stored a little differently to how we want them, so I process them here with regex
    '''
    releaseDates = []
    all_tr = infoSoup.find_all('tr')    #saving all table rows to this, can iterate through them
    for tr in all_tr:
        if tr.th != None:
            if tr.th.string == "Release date":
                li = tr.th.next_sibling.find_all('li')
                for tag in li:
                    dateBlob = tag.get_text()   #this comes in a weird format from which date and location need to be extracted 
                    date = re.search("(\(\d{4}-\d{2}-\d{2})\s*(\D+)?", dateBlob) # -->format will be: (yyyy-mm-dd) (location)
                    releaseDates.append(date.group(0))
    return(releaseDates)

def findStars(infoSoup):
    '''
    Stars are stored in either the 'li' tag or the 'a' or in the 'td' tag itself- different layers of nesting
    '''
    stars = []
    all_tr = infoSoup.find_all('tr')    #saving all table rows to this, can iterate through them
    for tr in all_tr:
        if tr.th != None:
            if tr.th.string == "Starring":
                li = tr.td.find_all('li')
                for tag in li:
                    stars.append(tag.string)
                if stars == []:
                    a = tr.td.find_all('a')
                    for tag in a:
                        stars.append(tag.string)
                    if stars == []:     # if we still havent found any stars, they must simply be in the top layer 'td'
                        stars.append(tr.td.string)
    return(stars)

def findPlot(soup):
    """
    This was tricky because for some or other reason wikipedia has decided not to hierarchically order paragraphs under headings
    like you would expect (heading > paragraph) but instead has them as siblings, which is what made it quite difficult to access 
    the three paragraphs that come right after the plot 'heading'
    """
    plot = ""
    rightDiv = None
    divs = soup.find_all('div')  # div is an identifiable tag
    for d in divs:
        if d(class_="mw-parser-output"):   # the dig we are looking for has this attribute
            rightDiv = d
    if rightDiv != None:
        siblings = rightDiv.find_all(['h2', 'p'])   # can find all headings (h2) and all paragraphs (p) under this div (remember, h2 and p are siblings)
        count = 0
        for tag in siblings:
            if tag(id="Plot"):
                count += 1
            if count > 0 and count <= 3:
                if tag.get_text() == "Cast[edit]":      #this seems to be the next heading under plot and we dont want it
                    break
                elif tag.get_text() == "Plot[edit]":
                    plot += "Plot" + "\n"
                else:
                    plot += tag.get_text() + "\n"
                count += 1
            elif count > 3:
                count = 0     # because we only want to get the first three siblings (including the "Plot" heading)
    return(plot)

def scrapeWikiMovie(url):
    res = requests.get(url)  # retrieves the page
    res.raise_for_status()   # checks for any errors
    wikiSoup = bs4.BeautifulSoup(res.text, "html.parser") # res.text is all text from page, html.parser helps to structure the text into html format
    infoTable = wikiSoup.find(class_="infobox vevent")
    
    directedBy = findDirector(infoTable)
    releaseDates = findReleaseDate(infoTable)
    movieName = findMovieName(infoTable)
    starring = findStars(infoTable)    # some of these still dont come out right
    plot = findPlot(wikiSoup)

    """
    some testing
    """
    if movieName == "" or movieName == None:
        print("Something wrong with movieName " + url)
        print("\n")
    if releaseDates == [] or releaseDates == None:
        print("Something wrong with releaseDates "+ url)
        print("\n")
    if starring == [] or starring == None:
        print("Something wrong with starring " + url)
        print("\n")

    print("Movie: " + movieName + "\n" + "Starring: " + str(starring) + "\n" + "Directed by: " + directedBy + "\n" + "Release date: " + str(releaseDates) + "\n")
    print("\n")
    print(plot)

#scrapeWikiMovie("https://en.wikipedia.org/wiki/Joker_(2019_film)")
#scrapeWikiMovie("https://en.wikipedia.org/wiki/Summertime_(2015_film)")
#scrapeWikiMovie("https://en.wikipedia.org/wiki/Pain_and_Glory")
#scrapeWikiMovie("https://en.wikipedia.org/wiki/Once_Upon_a_Time_in_Hollywood")


f = open('movienames.txt', 'r')
text = f.readline()
f.close()
txtList = text.split(";")
movieList = []
for movie in txtList:
    movieList.append(movie.replace(" ", "_"))   #prepping for the url

for movie in movieList:
    scrapeWikiMovie("https://en.wikipedia.org/wiki/" + movie)
