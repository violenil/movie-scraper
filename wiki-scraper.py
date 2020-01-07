import sys
import requests  # to download
import bs4
import csv


def scrapeWikiMovie(url):
    res = requests.get(url)  # retrieces the page
    res.raise_for_status()   # checks for any errors
    wikiSoup = bs4.BeautifulSoup(res.text, "html.parser") # res.text is all text from page, html.parser helps to structure the text into html format
    wikiContents = []
    infoTable = wikiSoup.find(class_="infobox vevent")
    directorTags= infoTable.find_all('')
    #print(directorTag)
    #directors = directorTag.find('td')
    #d = directors.getText()
    #print(d)

scrapeWikiMovie("https://en.wikipedia.org/wiki/Once_Upon_a_Time_in_Hollywood")
