# Python 3.11.1
# 2024-03-07

## Imports  ##
import json
import requests

requests.packages.urllib3.disable_warnings()
import xmltodict
import asyncio
import aiohttp
from xml.dom import minidom
import html
import os
import time
from html import unescape  # Adicionando a importação da função unescape
import logging
import warnings  # Erro falso positivo

warnings.filterwarnings("ignore", category=DeprecationWarning)
from PIL import Image
import re


def findWholeWord(w):
    return re.compile(r"\b({0})\b".format(w), flags=re.IGNORECASE).search


## Functions ##

# Setup logging basic conf
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    filename="feed.log",
    datefmt="%Y-%m-%d %H:%M:%S",
)


def getBlockedWords(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()

    else:

        logging.error("Failed to get blocked words from {}".format(url))
    return data


def getxml():
    url = "https://conectaverde.com.br/rss"
    ua = "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7"
    response = requests.get(url, headers={"User-Agent": ua})
    if response.status_code == 200:
        data = xmltodict.parse(response.content)
        # Log success
        logging.info("Success on getting xml from {}".format(url))
    else:
        # Log error
        logging.error("Failed to get xml from {}".format(url))
    return data


# Global variables #
global nowtime
nowtime = time.time()
global imagesToDownload
imagesToDownload = []


## Transform downloadImages and buildXML into one async function ##
def main():
    # Check if ./images/ folder exists
    if not os.path.exists("./images/"):
        os.makedirs("./images/")
    global imagesToDownload, nowtime
    data = getxml()
    doc = minidom.Document()
    rss = doc.createElement("rss")
    rss.setAttribute("version", "2.0")
    doc.appendChild(rss)
    updtime = doc.createElement("time")
    rss.appendChild(updtime)
    # Log start time
    now = time.ctime(nowtime)
    # print(now)
    logging.info("Start time main: {}".format(now))
    updtime.appendChild(doc.createTextNode(now))
    channel = doc.createElement("channel")
    rss.appendChild(channel)
    indexXml = 0
    for item in data["rss"]["channel"]["item"]:
        if indexXml > 10:
            break
        # Filter item description if contains blocked words from ../../utils/blocked_words.json #
        # Get blocked words #
        blocked_words = getBlockedWords(
            "http://combosmart.com/rsspanel/blocked_words.json"
        )
        blocked_words = blocked_words["default_words"]
        addItem = True

        for word in blocked_words:
            if findWholeWord(word)(item["title"]):
                print("Blocked word found: {}".format(word))
                addItem = False
            if findWholeWord(word)(item["description"]):
                print("Blocked word found: {}".format(word))
                addItem = False
        if addItem != False:
            category = doc.createElement("category")
            category.appendChild(doc.createTextNode(item["category"][0]))
            logCategory = str(item["category"][0])
            title = doc.createElement("title")
            title.appendChild(doc.createTextNode(item["title"]))
            logTitle = str(item["title"])
            description = doc.createElement("description")
            splited_description = item["description"].split("<p>")
            splited_description = splited_description[1].split("</p>")
            splited_description = splited_description[0].split("<br />")
            description.appendChild(doc.createTextNode(splited_description[0]))
            logDescription = str(splited_description[0])
            item = doc.createElement("item")
            item.appendChild(title)
            item.appendChild(description)
            item.appendChild(category)
            channel.appendChild(item)
            indexXml += 1
            # Log title, description #
            logging.info("Title: {} | Description: {}".format(logTitle, logDescription))
    # Save feed.xml UTF8 #
    with open("feed.xml", "w", encoding="utf-8") as f:
        f.write(doc.toprettyxml(indent="  ", encoding="utf-8").decode("utf-8"))
        # Log done time
        now = time.ctime(time.time())
        logging.info("Done time main: {}".format(now))


if __name__ == "__main__":

    main()
