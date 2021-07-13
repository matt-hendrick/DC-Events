import requests
from bs4 import BeautifulSoup
import json
from dateutil import parser
from datetime import datetime


def heritage_scraper():

    eventList = []

    url = "https://www.heritage.org/events"

    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    for event in soup.find_all("section", class_="result-card result-card__event result-card__event--upcoming result-card__event--has-video"):
        title = event.find(
            "div", class_="result-card__info-wrapper").get_text().strip()
        dateTime = str(parser.parse((event.find(
            "p", class_="result-card__event-date").get_text()) + " " + str(datetime.now().year) + " " + event.find(
            "p", class_="result-card__time").get_text()[:7]))
        entity = "The Heritage Foundation"
        entityType = "Think Tank"
        link = "https://www.heritage.org" + event.find(
            "div", class_="result-card__info-wrapper").find("a").get("href")
        eventList.append({"entity": entity, "type": entityType,
                         "dateTime": dateTime, "title": title, "link": link})

    filename = "event_list.json"
    with open(filename, "r") as file:
        data = json.load(file)

    for item in eventList:
        data.append(item)

    with open(filename, "w") as file:
        json.dump(data, file)


heritage_scraper()
