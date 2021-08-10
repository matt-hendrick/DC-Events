from dateutil import parser
import uuid
import datetime

from get_soup import get_soup


def cap_scraper():

    eventList = []

    soup = get_soup("https://www.americanprogress.org/events/upcoming-events/")

    for event in soup.find_all("article"):
        dateTime = parser.parse(event.find(
            "div", class_="entry-meta event-entry-meta-list").get_text()[:-13])
        if (dateTime > dateTime.now()):
            title = event.find("h3").get_text()
            dateTime = str(dateTime)
            date = datetime.datetime.strptime(dateTime, "%Y-%m-%d %H:%M:%S")
            unixTimeStamp = int(datetime.datetime.timestamp(date))
            entity = "The Center for American Progress"
            entityType = "Think Tank"
            link = event.find("a").get("href")
            eventID = str(uuid.uuid4())
            eventList.append({"entity": entity, "type": entityType,
                              "dateTime": dateTime, "title": title, "link": link, "eventID": eventID, "unixTimeStamp": unixTimeStamp})

    return eventList


if __name__ == "__main__":
    cap_scraper()
