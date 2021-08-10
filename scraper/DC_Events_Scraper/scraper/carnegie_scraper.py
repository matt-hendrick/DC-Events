from dateutil import parser
import uuid
import datetime

from get_soup import get_soup


def carnegie_scraper():

    eventList = []

    soup = get_soup("https://carnegieendowment.org/events")

    soup = soup.find(
        "div", class_="section foreground future-events no-margin-bottom")

    for event in soup.find_all("div", class_="interior"):
        title = event.find("h3").get_text()
        dateTime = str(parser.parse(event.find(
            "div", class_="date").get_text() + " " + event.find(
            "div", class_="time").get_text()[:7]))
        date = datetime.datetime.strptime(dateTime, "%Y-%m-%d %H:%M:%S")
        unixTimeStamp = int(datetime.datetime.timestamp(date))
        entity = "Carnegie Endowment for International Peace"
        entityType = "Think Tank"
        link = "https://carnegieendowment.org" + event.find("a").get("href")
        eventID = uuid.uuid4()
        eventList.append({"entity": entity, "type": entityType,
                          "dateTime": dateTime, "title": title, "link": link, "eventID": eventID, "unixTimeStamp": unixTimeStamp})

    for event in soup.find_all("div", class_="cols"):
        title = event.find("h3").get_text()
        dateTime = str(parser.parse(event.find(
            "span", class_="month is-ts").get_text() + " " + event.find(
            "span", class_="day").get_text() + " " + event.find(
            "span", class_="year").get_text()))
        date = datetime.datetime.strptime(dateTime, "%Y-%m-%d %H:%M:%S")
        unixTimeStamp = int(datetime.datetime.timestamp(date))
        entity = "Carnegie Endowment for International Peace"
        entityType = "Think Tank"
        link = "https://carnegieendowment.org" + event.find("a").get("href")
        eventID = str(uuid.uuid4())
        eventList.append({"entity": entity, "type": entityType,
                          "dateTime": dateTime, "title": title, "link": link, "eventID": eventID, "unixTimeStamp": unixTimeStamp})

    return eventList


if __name__ == "__main__":
    carnegie_scraper()
