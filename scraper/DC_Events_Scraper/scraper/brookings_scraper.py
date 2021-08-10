from dateutil import parser
import uuid
import datetime

from get_soup import get_soup


def brookings_scraper():
    eventList = []

    soup = get_soup("https://www.brookings.edu/events/upcoming/")

    for event in soup.find_all("a", class_="event-content"):
        title = event.find("h4").get_text()
        dateTime = str(parser.parse(event.find(
            "div", class_="event-date list").get("content")[0:19]))
        date = datetime.datetime.strptime(dateTime, "%Y-%m-%d %H:%M:%S")
        unixTimeStamp = int(datetime.datetime.timestamp(date))
        entity = "The Brookings Institution"
        entityType = "Think Tank"
        link = event.get("href")
        eventID = str(uuid.uuid4())
        eventList.append({"entity": entity, "type": entityType,
                         "dateTime": dateTime, "title": title, "link": link, "eventID": eventID, "unixTimeStamp": unixTimeStamp})

    return eventList


if __name__ == "__main__":
    brookings_scraper()
