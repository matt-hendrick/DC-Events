import requests
from bs4 import BeautifulSoup
import json
from dateutil import parser
import uuid


def brookings_scraper():

    eventList = []

    url = "https://www.brookings.edu/events/upcoming/"

    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    for event in soup.find_all("a", class_="event-content"):
        title = event.find("h4").get_text()
        dateTime = parser.parse(event.find(
            "div", class_="event-date list").get("content"))
        entity = "The Brookings Institution"
        entityType = "Think Tank"
        link = event.get("href")
        eventID = str(uuid.uuid4())
        eventList.append({"entity": entity, "type": entityType,
                         "dateTime": dateTime, "title": title, "link": link, "eventID": eventID})

    return eventList


if __name__ == "__main__":
    brookings_scraper()
