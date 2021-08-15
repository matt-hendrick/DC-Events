from dateutil import parser
import uuid
import datetime

from get_soup import get_soup


def wapo_scraper():
    eventList = []

    soup = get_soup("https://www.washingtonpost.com/washington-post-live/")

    # gets lede/highlighted event
    soup1 = soup.find(attrs={"data-feature-name": "lede-article"})

    # gets remainder of upcoming events
    soup2 = soup.find(attrs={"data-feature-name": "upcoming-shows"})

    for event in soup1.find_all("div", class_="border-top-off border-top-100-pct border-bottom-hairline border-bottom-100-pct"):
        dateTime = event.find(
            "li", class_="display-date")
        if dateTime != None:
            dateTime = parser.parse(dateTime.get_text())
            if dateTime > dateTime.now():
                title = event.find("h2").get_text()
                dateTime = str(dateTime)
                date = datetime.datetime.strptime(
                    dateTime, "%Y-%m-%d %H:%M:%S")
                unixTimeStamp = int(datetime.datetime.timestamp(date))
                entity = "The Washington Post"
                entityType = "Newspaper"
                link = event.find(
                    "h2").find("a").get("href")
                additionalInfo = None
                eventID = str(uuid.uuid4())
                eventList.append({"entity": entity, "type": entityType,
                                  "dateTime": dateTime, "title": title, "link": link, "additionalInfo": additionalInfo, "eventID": eventID, "unixTimeStamp": unixTimeStamp})

    for event in soup2.find_all("div", class_="border-top-off border-top-100-pct border-bottom-hairline border-bottom-100-pct"):
        dateTime = event.find(
            "li", class_="display-date")
        if dateTime != None:
            dateTime = parser.parse(dateTime.get_text())
            if dateTime > dateTime.now():
                title = event.find("h2").get_text()
                dateTime = str(dateTime)
                date = datetime.datetime.strptime(
                    dateTime, "%Y-%m-%d %H:%M:%S")
                unixTimeStamp = int(datetime.datetime.timestamp(date))
                entity = "The Washington Post"
                entityType = "Newspaper"
                link = event.find(
                    "h2").find("a").get("href")
                additionalInfo = None
                eventID = str(uuid.uuid4())
                eventList.append({"entity": entity, "type": entityType,
                                  "dateTime": dateTime, "title": title, "link": link, "additionalInfo": additionalInfo, "eventID": eventID, "unixTimeStamp": unixTimeStamp})

    return eventList


if __name__ == "__main__":
    wapo_scraper()
