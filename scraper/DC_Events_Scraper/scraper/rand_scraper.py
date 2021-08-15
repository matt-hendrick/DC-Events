from dateutil import parser
import uuid
import datetime

from get_soup import get_soup


def rand_scraper():

    eventList = []

    soup = get_soup("https://www.rand.org/events.html")

    for event in soup.find_all("div", class_="text"):
        if (event.find("p", class_="date")):
            dateTime = parser.parse(event.find(
                "p", class_="date").get_text())
            # Only writes event to DB if it is a future event
            if (dateTime > dateTime.now()):
                title = event.find("h3").get_text()
                dateTime = str(dateTime)
                date = datetime.datetime.strptime(
                    dateTime, "%Y-%m-%d %H:%M:%S")
                unixTimeStamp = int(datetime.datetime.timestamp(date))
                entity = "RAND Corporation"
                entityType = "Think Tank"
                link = event.find("a").get("href")
                eventID = str(uuid.uuid4())
                additionalInfo = None
                eventList.append({"entity": entity, "type": entityType,
                                  "dateTime": dateTime, "title": title, "link": link, "additionalInfo": additionalInfo, "eventID": eventID, "unixTimeStamp": unixTimeStamp})

    return eventList


if __name__ == "__main__":
    rand_scraper()
