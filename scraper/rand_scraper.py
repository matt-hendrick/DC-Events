import requests
from bs4 import BeautifulSoup
import json
from dateutil import parser


def rand_scraper():

    eventList = []

    url = "https://www.rand.org/events.html"

    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    for event in soup.find_all("div", class_="text"):
        if (event.find("p", class_="date")):
            dateTime = parser.parse(event.find(
                "p", class_="date").get_text())
            if (dateTime > dateTime.now()):
                title = event.find("h3").get_text()
                dateTime = str(dateTime)
                entity = "RAND Corporation"
                entityType = "Think Tank"
                link = event.find("a").get("href")
                eventList.append({"entity": entity, "type": entityType,
                                  "dateTime": dateTime, "title": title, "link": link})

    return eventList


if __name__ == "__main__":
    rand_scraper()
