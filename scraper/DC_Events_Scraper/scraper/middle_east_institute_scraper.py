import requests
from bs4 import BeautifulSoup
import json
from dateutil import parser
import uuid
import datetime


def middle_east_institute_scraper():

    eventList = []

    url = "https://www.mei.edu/events"

    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    for event in soup.find_all("div", class_="related-event-feature"):
        dateTime = parser.parse(event.find(
            "div", class_="feature__date").get_text())
        if (dateTime > dateTime.now()):
            title = event.find("h4").get_text()
            dateTime = str(dateTime)
            date = datetime.datetime.strptime(dateTime, "%Y-%m-%d %H:%M:%S")
            unixTimeStamp = int(datetime.datetime.timestamp(date))
            entity = "Middle East Institute"
            entityType = "Think Tank"
            link = event.find("a").get("href")
            eventID = str(uuid.uuid4())
            eventList.append({"entity": entity, "type": entityType,
                              "dateTime": dateTime, "title": title, "link": link, "eventID": eventID, "unixTimeStamp": unixTimeStamp})

    return eventList


if __name__ == "__main__":
    middle_east_institute_scraper()
