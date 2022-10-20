import os
import requests
import time
import random
import datetime

from datetime import datetime
from threading import Timer
from bs4 import BeautifulSoup
from flask import Flask, request


app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return "Where my bot for Montgomery Hall lives :) - Jason, implementing SSL soon"


# print() are in the log file
@app.route("/", methods=["POST"])
def receive():
    print("Incoming message:")
    data = request.get_json()
    print(data)

    # prevent self-reply
    if data["sender_type"] != "RA BOT":
        read(data["text"].lower())

        if data["text"].startswith("/ping"):
            send(data["name"] + " pinged me!")

    return "ok", 200


# happens everyday, using the timer at the bottom
def update():
    getFood()
    goodMorning()


def goodMorning():
    send("Good Morning Montgomery Hall")


def showMenu():
    return """RA BOT MENU: \n
             You can send the bot a command! \n
             Upcoming Events: /events \n
             Is Jason on Duty right now?: /duty? \n
             Pick a num between 1-10: /pick \n
             Flip a coin: /flip \n
             Phone Numbers: /numbers \n"""


def readEvents():
    with open("events.txt") as f:
        send("".join(f.readlines()))


def readFood():
    with open("food.txt") as f:
        send("".join(f.readlines()))


# scrapes data from umd dining menu
def getFood():
    page = requests.get("http://nutrition.umd.edu/")  # not secured smh
    soup = BeautifulSoup(page.content, "html.parser")
    elements = soup.find_all("a")
    food = set()

    for i in range(12, len(elements)):
        item = str(elements[i])
        item = item[item.find(">") + 1 :].replace(
            "</a>", ""
        )  # locate food, and remove tags

        # don't add the leftover tags
        if not (
            item.startswith(" <span") or item.startswith("(") or item.startswith("http")
        ):
            food.add(item)

    f = open("food.txt", "w")
    for item in food:
        f.write(item + "\n")

    return food


def chicken_tenders(food):
    if "Chicken Tenders" in food:
        return True
    return False


def read(msg):
    text = msg.split(" ")

    if msg == "/menu":
        send(showMenu())
    elif msg == "/events":
        send(readEvents())
    elif msg == "/duty?":
        # pulls data from Google Calendar API
        send("No")
    elif msg == "/pick":
        send(str(random.randint(1, 10)))
    elif msg == "/flip":
        toss = random.randint(1, 2)
        if toss == 1:
            send("tails")
        else:
            send("heads")
    elif msg == "/numbers":
        # numbers() -> not shown for sake of confidentality
        send(numbers)
    elif msg == "/food":
        readFood()
    elif msg == "/tendies":
        food = getFood()
        if chicken_tenders(food):
            send("CHICKEN TENDERS @ 12")
        else:
            send("Sorry, not today")

    return True


def send(msg):
    url = "https://api.groupme.com/v3/bots/post"

    data = {
        "bot_id": os.getenv("GROUPME_BOT_ID"),
        "text": msg,
    }
    # sends message to GroupMe
    r = requests.post(url, json=data)


while True:
    present = datetime.today()
    nextDay = present.replace(day=present.day + 1, hour=6, minute=0, second=0)
    changeTime = nextDay - present

    t = Timer(changeTime, update())
    t.start()
