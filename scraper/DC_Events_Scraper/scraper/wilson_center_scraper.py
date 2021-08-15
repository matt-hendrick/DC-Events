from dateutil import parser
import uuid
import datetime

from get_soup import get_soup


def wilson_center_scraper():

    eventList = []

    soup = get_soup("https://www.wilsoncenter.org/events")

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
        additionalInfo = None
        eventID = str(uuid.uuid4())
        eventList.append({"entity": entity, "type": entityType,
                         "dateTime": dateTime, "title": title, "link": link, "additionalInfo": additionalInfo, "eventID": eventID, "unixTimeStamp": unixTimeStamp})

    print(eventList)
    return eventList


if __name__ == "__main__":
    wilson_center_scraper()
