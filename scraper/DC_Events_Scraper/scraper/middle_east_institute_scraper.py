from dateutil import parser
import uuid
import datetime

from get_soup import get_soup


def middle_east_institute_scraper():

    eventList = []

    soup = get_soup("https://www.mei.edu/events")

    for event in soup.find_all("div", class_="related-event-feature"):
        dateTime = parser.parse(event.find(
            "div", class_="feature__date").get_text())
        # Only writes event to DB if it is a future event
        if dateTime > dateTime.now():
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
