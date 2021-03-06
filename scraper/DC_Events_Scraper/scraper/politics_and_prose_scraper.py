from dateutil import parser
import uuid
import datetime

from get_soup import get_soup


def politics_and_prose_scraper():
    eventList = []

    soup = get_soup("https://www.politics-prose.com/events/detailed-list")

    soup = soup.find("div", class_="region region-content")

    for event in soup.find_all("div", class_="views-row"):
        title = event.find("h2").get_text()
        if len(event.find(
                "div", class_="views-field views-field-field-date").get_text().split()) < 5:
            dateTime = str(parser.parse(event.find(
                "div", class_="views-field views-field-field-date").get_text()))
        # if len is > 5, date is a range which the parser cannot handle
        # splits date text and only returns first 4
        else:
            dateTime = str(parser.parse((" ".join(event.find(
                "div", class_="views-field views-field-field-date").get_text().split()[0:5]))))
        date = datetime.datetime.strptime(dateTime, "%Y-%m-%d %H:%M:%S")
        unixTimeStamp = int(datetime.datetime.timestamp(date))
        entity = "Politics and Prose"
        entityType = "Bookstore"
        # P&P event links are eventbrite links
        if len([a['href'] for a in event.select("a[href*=eventbrite]")]) > 0:
            link = [a['href'] for a in event.select("a[href*=eventbrite]")][0]
        # if there is no eventbrite link, add other link (if available)
        elif event.find("a").get("href") != None:
            link = event.find("a").get("href")
        else:
            link: "https://www.politics-prose.com/events"
        additionalInfo = None
        eventID = str(uuid.uuid4())
        eventList.append({"entity": entity, "type": entityType,
                         "dateTime": dateTime, "title": title, "link": link, "additionalInfo": additionalInfo, "eventID": eventID, "unixTimeStamp": unixTimeStamp})

    return eventList


if __name__ == "__main__":
    politics_and_prose_scraper()
