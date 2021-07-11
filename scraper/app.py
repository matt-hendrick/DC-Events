import requests
from bs4 import BeautifulSoup
import json
import re
import time

eventList = {}

url = "https://www.brookings.edu/events/upcoming/"

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

dates = []

for event in soup.find_all("a", class_="event-content"):
    title = event.find("h4").get_text()
    date = event.find("div", class_="date-day").get_text() + " " + event.find("div",
                                                                              class_="date-month").get_text() + " " + event.find("div", class_="date-number").get_text()
    time = event.find_all("time")[0].get_text(
    ).strip() + " - " + event.find_all("time")[1].get_text().strip()
    link = event.get("href")
    eventList[title] = {"date": date,
                        "time": time, "title": title, "link": link}


json_string = json.dumps(eventList)


with open("eventList.json", "w") as outfile:
    outfile.write(json_string)
