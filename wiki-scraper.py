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
    releaseDates = [] 

    all_tr = infoTable.find_all('tr')    #saving all table rows to this, can iterate through them
    for tr in all_tr:
        if tr.th != None:
            if tr.th.string == "Directed by":
                directedBy = tr.th.next_sibling.string
            if tr.th.string == "Release date":
                li = tr.th.next_sibling.find_all('li')
                for tag in li:
                    releaseDates.append(tag.get_text())

    print("Movie: " + movieName + "\n" + "Directed by: " + directedBy + "\n" + "Release date: " + str(releaseDates) + "\n")

scrapeWikiMovie("https://en.wikipedia.org/wiki/Cold_War_(2018_film)")
