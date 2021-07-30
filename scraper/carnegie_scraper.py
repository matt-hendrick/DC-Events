import requests
from bs4 import BeautifulSoup
import json
from dateutil import parser


def carnegie_scraper():

    eventList = []

    url = "https://carnegieendowment.org/events"

    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    soup = soup.find(
        "div", class_="section foreground future-events no-margin-bottom")

    for event in soup.find_all("div", class_="interior"):
        title = event.find("h3").get_text()
        dateTime = str(parser.parse(event.find(
            "div", class_="date").get_text() + " " + event.find(
            "div", class_="time").get_text()[:7]))
        entity = "Carnegie Endowment for International Peace"
        entityType = "Think Tank"
        link = "https://carnegieendowment.org" + event.find("a").get("href")
        eventList.append({"entity": entity, "type": entityType,
                          "dateTime": dateTime, "title": title, "link": link})

    for event in soup.find_all("div", class_="cols"):
        title = event.find("h3").get_text()
        dateTime = str(parser.parse(event.find(
            "span", class_="month is-ts").get_text() + " " + event.find(
            "span", class_="day").get_text() + " " + event.find(
            "span", class_="year").get_text()))
        entity = "Carnegie Endowment for International Peace"
        entityType = "Think Tank"
        link = "https://carnegieendowment.org" + event.find("a").get("href")
        eventList.append({"entity": entity, "type": entityType,
                          "dateTime": dateTime, "title": title, "link": link})
    print(eventList)
    return eventList


if __name__ == "__main__":
    carnegie_scraper()
