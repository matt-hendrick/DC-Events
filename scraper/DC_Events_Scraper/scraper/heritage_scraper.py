from dateutil import parser
import datetime
import uuid

from get_soup import get_soup


def heritage_scraper():

    eventList = []

    soup = get_soup("https://www.heritage.org/events")

    for event in soup.find_all("section", class_="result-card result-card__event result-card__event--upcoming result-card__event--has-video"):
        title = event.find(
            "div", class_="result-card__info-wrapper").get_text().strip()
        dateTime = str(parser.parse((event.find(
            "p", class_="result-card__event-date").get_text()) + " " + str(datetime.datetime.now().year) + " " + event.find(
            "p", class_="result-card__time").get_text()[:7]))
        date = datetime.datetime.strptime(dateTime, "%Y-%m-%d %H:%M:%S")
        unixTimeStamp = int(datetime.datetime.timestamp(date))
        entity = "The Heritage Foundation"
        entityType = "Think Tank"
        link = "https://www.heritage.org" + event.find(
            "div", class_="result-card__info-wrapper").find("a").get("href")
        eventID = str(uuid.uuid4())
        eventList.append({"entity": entity, "type": entityType,
                          "dateTime": dateTime, "title": title, "link": link, "eventID": eventID, "unixTimeStamp": unixTimeStamp})

    return eventList


if __name__ == "__main__":
    heritage_scraper()
