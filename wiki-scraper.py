import sys
import requests  # to download
import bs4
import csv


def scrapeWikiMovie(url):
    res = requests.get(url)  # retrieves the page
    res.raise_for_status()   # checks for any errors
    wikiSoup = bs4.BeautifulSoup(res.text, "html.parser") # res.text is all text from page, html.parser helps to structure the text into html format
    infoTable = wikiSoup.find(class_="infobox vevent")
    
    directedBy = ""
    movieName = infoTable.tr.string
    releaseDates = [] 
    starring = []    # some of these still dont come out right
    plot = ""

    all_tr = infoTable.find_all('tr')    #saving all table rows to this, can iterate through them
    for tr in all_tr:
        if tr.th != None:
            if tr.th.string == "Directed by":
                directedBy = tr.th.next_sibling.string
            if tr.th.string == "Release date":
                li = tr.th.next_sibling.find_all('li')
                for tag in li:
                    releaseDates.append(tag.get_text())
            if tr.th.string == "Starring":
                li = tr.td.find_all('li')
                for tag in li:
                    starring.append(tag.string)

    print("Movie: " + movieName + "\n" + "Directed by: " + directedBy + "\n" + "Release date: " + str(releaseDates) + "\n")
    print("Starring: " + str(starring))

f = open('movienames.txt', 'r')
text = f.readline()
f.close()
txtList = text.split(";")
movieList = []
for movie in txtList:
    movieList.append(movie.replace(" ", "_"))   #prepping for the url

for movie in movieList:
    scrapeWikiMovie("https://en.wikipedia.org/wiki/" + movie)
