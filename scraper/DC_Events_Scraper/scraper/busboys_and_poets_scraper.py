from dateutil import parser
import uuid
import datetime

from get_soup import get_soup


def busboys_and_poets_scraper():
    eventList = []

    soup = get_soup("https://www.busboysandpoets.com/events-list/")

    for event in soup.find_all("div", class_="event-tile"):
        title = event.find("h3").get_text()
        dateTime = str(parser.parse(event.find(
            "p", class_="event-date").get_text()))
        date = datetime.datetime.strptime(dateTime, "%Y-%m-%d %H:%M:%S")
        unixTimeStamp = int(datetime.datetime.timestamp(date))
        entity = "Busboys and Poets"
        entityType = "Bookstore"
        link = event.find("a").get("href")
        additionalInfo = event.find(
            "p", class_="event-meta").get_text()
        eventID = str(uuid.uuid4())
        eventList.append({"entity": entity, "type": entityType,
                         "dateTime": dateTime, "title": title, "link": link, "additionalInfo": additionalInfo, "eventID": eventID, "unixTimeStamp": unixTimeStamp})

    return eventList


if __name__ == "__main__":
    busboys_and_poets_scraper()
