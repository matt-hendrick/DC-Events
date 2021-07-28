import requests
from bs4 import BeautifulSoup
import json
from dateutil import parser


def atlantic_council_scraper():

    eventList = []

    url = "https://www.atlanticcouncil.org/events/"

    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    for event in soup.find_all("div", class_="gta-embed--content gta-event-embed--content"):
        title = event.find("h3").get_text().strip()
        dateTime = str(parser.parse(event.find(
            "p", class_="gta-event-embed--heading gta-embed--heading s-tag-button").get_text() + " " + event.find("span").get_text()))
        entity = "The Atlantic Council"
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
    atlantic_council_scraper()
