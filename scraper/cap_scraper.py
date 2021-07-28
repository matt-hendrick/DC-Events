import requests
from bs4 import BeautifulSoup
import json
from dateutil import parser


def cap_scraper():

    eventList = []

    url = "https://www.americanprogress.org/events/upcoming-events/"

    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    for event in soup.find_all("article"):
        dateTime = parser.parse(event.find(
            "div", class_="entry-meta event-entry-meta-list").get_text()[:-13])
        if (dateTime > dateTime.now()):
            title = event.find("h3").get_text()
            dateTime = str(dateTime)
            entity = "The Center for American Progress"
            entityType = "Think Tank"
            link = event.find("a").get("href")
            eventList.append({"entity": entity, "type": entityType,
                              "dateTime": dateTime, "title": title, "link": link})

    filename = "event_list.json"
    with open(filename, "r") as file:
        data = json.load(file)

    for item in eventList:
        data.append(item)

    with open(filename, "w") as file:
        json.dump(data, file)


if __name__ == "__main__":
    cap_scraper()
