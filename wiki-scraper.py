import sys
import requests  # to download
import bs4
import csv


def scrapeWikiMovie(url):
    res = requests.get(url)  # retrieces the page
    res.raise_for_status()   # checks for any errors
    wikiSoup = bs4.BeautifulSoup(res.text, "html.parser") # res.text is all text from page, html.parser helps to structure the text into html format
    infoTable = wikiSoup.find(class_="infobox vevent")
    
    directedBy = ""
    movieName = infoTable.tr.string

    all_tr = infoTable.find_all('tr')
    for tr in all_tr:
        if tr.th != None:
            if tr.th.string == "Directed by":
                directedBy = tr.th.next_sibling.string
    print("Movie: " + movieName + "\n" + "Directed by: " + directedBy)

scrapeWikiMovie("https://en.wikipedia.org/wiki/Once_Upon_a_Time_in_Hollywood")
