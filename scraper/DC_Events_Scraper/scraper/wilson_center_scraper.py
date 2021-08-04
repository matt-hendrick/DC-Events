import requests
from bs4 import BeautifulSoup
import json
from dateutil import parser
import uuid
import datetime


def wilson_center_scraper():

    eventList = []

    url = "https://www.wilsoncenter.org/events"

    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    for event in soup.find_all("div", class_="faceted-search-event"):
        title = event.find("h4").get_text().strip()
        dateTime = str(parser.parse(event.find(
            "div", class_="faceted-search-event-date").get_text() + " " + event.find(
            "div", class_="faceted-search-event-time").get_text()[:20], fuzzy=True))
        date = datetime.datetime.strptime(dateTime, "%Y-%m-%d %H:%M:%S")
        unixTimeStamp = int(datetime.datetime.timestamp(date))
        entity = "The Wilson Center"
        entityType = "Think Tank"
        link = "https://www.wilsoncenter.org" + \
            event.find("a").get("href")
        eventID = str(uuid.uuid4())
        eventList.append({"entity": entity, "type": entityType,
                         "dateTime": dateTime, "title": title, "link": link, "eventID": eventID, "unixTimeStamp": unixTimeStamp})

    return eventList


if __name__ == "__main__":
    wilson_center_scraper()
