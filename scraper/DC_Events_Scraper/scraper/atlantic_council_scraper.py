import requests
from bs4 import BeautifulSoup
import json
from dateutil import parser
import uuid
import datetime


def atlantic_council_scraper():

    eventList = []

    url = "https://www.atlanticcouncil.org/events/"

    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    for event in soup.find_all("div", class_="gta-embed--content gta-event-embed--content"):
        title = event.find("h3").get_text().strip()
        dateTime = str(parser.parse(event.find(
            "p", class_="gta-event-embed--heading gta-embed--heading s-tag-button").get_text() + " " + event.find("span").get_text()))
        date = datetime.datetime.strptime(dateTime, "%Y-%m-%d %H:%M:%S")
        unixTimeStamp = int(datetime.datetime.timestamp(date))
        entity = "The Atlantic Council"
        entityType = "Think Tank"
        link = event.find("a").get("href")
        eventID = str(uuid.uuid4())
        eventList.append({"entity": entity, "type": entityType,
                         "dateTime": dateTime, "title": title, "link": link, "eventID": eventID, "unixTimeStamp": unixTimeStamp})

    return eventList


if __name__ == "__main__":
    atlantic_council_scraper()
