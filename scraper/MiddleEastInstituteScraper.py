import requests
from bs4 import BeautifulSoup
import json
from dateutil import parser


def MEIScraper():

    eventList = []

    url = "https://www.mei.edu/events"

    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    for event in soup.find_all("div", class_="related-event-feature"):
        dateTime = parser.parse(event.find(
            "div", class_="feature__date").get_text())
        if (dateTime > dateTime.now()):
            title = event.find("h4").get_text()

            dateTime = str(dateTime)
            entity = " Middle East Institute"
            type = "Think Tank"
            link = event.find("a").get("href")
            eventList.append({"entity": entity, "type": type,
                              "dateTime": dateTime, "title": title, "link": link})

    filename = "eventList.json"
    with open(filename, "r") as file:
        data = json.load(file)

    for item in eventList:
        data.append(item)

    with open(filename, "w") as file:
        json.dump(data, file)

    # with open("eventList.json", "a") as outfile:
    #     outfile.write(json_string)


MEIScraper()
