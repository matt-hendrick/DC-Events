import requests
from bs4 import BeautifulSoup
import json
from dateutil import parser


def csis_scraper():

    eventList = []

    url = "https://www.csis.org/events-upcoming?title="

    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    for event in soup.find_all("div", class_="ds-right"):
        title = event.find("div", class_="teaser__title").get_text()
        dateTime = str(parser.parse(event.find(
            "span", class_="date-display-single").get("content")))
        entity = "CSIS"
        entityType = "Think Tank"
        link = "https://www.csis.org" + event.find("a").get("href")
        eventList.append({"entity": entity, "type": entityType,
                         "dateTime": dateTime, "title": title, "link": link})

    return eventList


if __name__ == "__main__":
    csis_scraper()
