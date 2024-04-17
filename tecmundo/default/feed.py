# # Python 3.11.1
# # 2024-03-07

# ## Imports  ##
# import json
# import requests
# requests.packages.urllib3.disable_warnings() 
# import xmltodict
# import asyncio
# import aiohttp
# from xml.dom import minidom
# import os
# import time
# import logging
# import warnings # Erro falso positivo
# warnings.filterwarnings("ignore", category=DeprecationWarning) 
# from PIL import Image
# import re
# def findWholeWord(w):
#     return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search
# ## Functions ##

# # Setup logging basic conf
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', filename='feed.log', datefmt='%Y-%m-%d %H:%M:%S')


# 
def getBlockedWords(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()

    else:

        logging.error("Failed to get blocked words from {}".format(url))
    return data

def getxml():
#     url = 'https://rss.tecmundo.com.br/feed/'
#     ua = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
#     response = requests.get(url, headers={"User-Agent": ua}, verify=False)
#     if response.status_code == 200:
#         data = xmltodict.parse(response.content)
#         # Log success
#         logging.info('Success on getting xml from {}'.format(url))
#     else:
#         # Log error
#         logging.error('Failed to get xml from {}'.format(url))
#     return data


# def buildXML():
#     data = getxml()
#     doc = minidom.Document()
#     rss = doc.createElement('rss')
#     rss.setAttribute('version', '2.0')
#     doc.appendChild(rss)
#     updtime = doc.createElement('time')
#     rss.appendChild(updtime)
#     # Get now time #
#     now = time.time()
#     now = time.ctime(now)
#     print(now)
#     # Log start time
#     logging.info('Start time: {}'.format(now))
#     updtime.appendChild(doc.createTextNode(now))
#     channel = doc.createElement('channel')
#     rss.appendChild(channel)
#     index = 0
#     for item in data['rss']['channel']['item']:
#         # Filter item description if contains blocked words from ../../utils/blocked_words.json #
#         # Get blocked words #
#         with open('../../utils/blocked_words.json', 'r', encoding='utf-8') as f:
#             blocked_words = json.load(f)
#             blocked_words = blocked_words['default_words']
#         addItem = True
#         # Filter description #
#         blocked_words = getBlockedWords(
            "http://combosmart.com/rsspanel/blocked_words.json"
        )
        blocked_words = blocked_words["default_words"]
        addItem = True
        for word in blocked_words:
#             if word in item['description']:
#                 addItem = False
#             if word in item['title']:
#                 addItem = False
#         if addItem != False:
#             # Title#
#             title = doc.createElement('title')
#             title.appendChild(doc.createTextNode(item['category']))
#             logTitle = item['category']
#             # Description #
#             description = doc.createElement('description')
#             description.appendChild(doc.createTextNode(item['title']))
#             logDescription = item['title']
#             # Path #
#             ## Image path = ./images/index.ext ##
#             # Get enclosure
#             url = item['enclosure']['@url']
#             logImage = url
#             # Get extension
#             ext = url.split('.')[-1]
#             # Create folder images if not exists
#             if not os.path.exists('./images/'):
#                 os.makedirs('./images/')
#             # Set filename index and ext
#             filename = f'./images/{index}.{ext}'
#             path = doc.createElement('linkfoto')
#             path.appendChild(doc.createTextNode(filename))
#             # Close item #
#             item = doc.createElement('item')
#             item.appendChild(title)
#             item.appendChild(description)
#             item.appendChild(path)
#             channel.appendChild(item)
#             index += 1
#             # Log item title, description and image url
#             logging.info('Title: {} Description: {} Image: {}'.format(logTitle, logDescription, logImage))

#     # Save feed.xml UTF8 #
#     with open('feed.xml', 'w', encoding='utf-8') as f:
#         f.write(doc.toprettyxml(indent='  ', encoding='utf-8').decode('utf-8'))


# async def downloadImages():
#     start_time = time.time()
#     ## Delete all files in folder async ##
#     await asyncio.gather(*[asyncio.to_thread(os.remove, f'./images/{file}') for file in os.listdir('./images')])
#     buildXML()
#     data = getxml()
#     index = 0
#     async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
#         for item in data['rss']['channel']['item']:
#             # Filter item description if contains blocked words from ../../utils/blocked_words.json #
#             # Get blocked words #
#             with open('../../utils/blocked_words.json', 'r', encoding='utf-8') as f:
#                 blocked_words = json.load(f)
#                 blocked_words = blocked_words['default_words']
#             addItem = True
#             # Filter description #
#             blocked_words = getBlockedWords(
            "http://combosmart.com/rsspanel/blocked_words.json"
        )
        blocked_words = blocked_words["default_words"]
        addItem = True
        for word in blocked_words:
#                 if word in item['description']:
#                     addItem = False
#             if addItem != False:
#                 url = item['enclosure']['@url']
#                 # Get extension
#                 ext = url.split('.')[-1]
#                 # Set filename index and ext
#                 filename = f'./images/{index}.{ext}'
#                 # Download image
#                 async with session.get(url) as response:
#                     content = await response.read()
#                     with open(filename, 'wb') as f:
#                         f.write(content)
#                         # Log Downloaded
#                         logging.info('Downloaded {} from {}'.format(filename, url))
#                     index += 1
#     # Print done with time #
#     print("Done! Took {} seconds".format(time.time() - start_time))
#     # Log done with time #
#     logging.info('Done! Took {} seconds'.format(time.time() - start_time))


# if __name__ == '__main__':
#     # Create folder images if not exists
#     if not os.path.exists('./images/'):
#         os.makedirs('./images/')
#         asyncio.run(downloadImages())
#     else:
#         asyncio.run(downloadImages())


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
import os
import time
import logging
import warnings # Erro falso positivo
warnings.filterwarnings("ignore", category=DeprecationWarning) 
from PIL import Image
import re
def findWholeWord(w):
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search
## Functions ##


# Setup logging basic conf
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', filename='feed.log', datefmt='%Y-%m-%d %H:%M:%S')

# Get xml from url

def getBlockedWords(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()

    else:

        logging.error("Failed to get blocked words from {}".format(url))
    return data

def getxml():
    url = 'https://rss.tecmundo.com.br/feed/'
    ua = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    response = requests.get(url, headers={"User-Agent": ua}, verify=False)
    if response.status_code == 200:
        data = xmltodict.parse(response.content)
        # Log success
        logging.info('Success on getting xml from {}'.format(url))
    else:
        # Log error
        logging.error('Failed to get xml from {}'.format(url))
    return data

# Global variables #
global nowtime
nowtime = time.time()
global imagesToDownload
imagesToDownload = []
## Transform downloadImages and buildXML into one async function ##
def main():
    # Check if ./images/ folder exists
    if not os.path.exists('./images/'):
        os.makedirs('./images/')
    global imagesToDownload, nowtime
    data = getxml()
    doc = minidom.Document()
    rss = doc.createElement('rss')
    rss.setAttribute('version', '2.0')
    doc.appendChild(rss)
    updtime = doc.createElement('time')
    rss.appendChild(updtime)
    # Log start time
    now = time.ctime(nowtime)
    # print(now)
    logging.info('Start time main: {}'.format(now))
    updtime.appendChild(doc.createTextNode(now))
    channel = doc.createElement('channel')
    rss.appendChild(channel)
    indexXml = 0
    for item in data['rss']['channel']['item']:
        if indexXml > 10:
            break
        # Filter item description if contains blocked words from ../../utils/blocked_words.json #
        # Get blocked words #
        with open('../../utils/blocked_words.json', 'r', encoding='utf-8') as f:
            blocked_words = json.load(f)
            blocked_words = blocked_words['default_words']
        addItem = True
        blocked_words = getBlockedWords(
            "http://combosmart.com/rsspanel/blocked_words.json"
        )
        blocked_words = blocked_words["default_words"]
        addItem = True
        for word in blocked_words:
            if findWholeWord(word)(item['title']):
                print('Blocked word found: {}'.format(word))
                addItem = False
            if findWholeWord(word)(item['description']):
                print('Blocked word found: {}'.format(word))
                addItem = False
        if addItem != False:
            # Title#
            title = doc.createElement('title')
            title.appendChild(doc.createTextNode(item['category']))
            logTitle = item['category']
            # Description #
            description = doc.createElement('description')
            description.appendChild(doc.createTextNode(item['title']))
            logDescription = item['title']
            # Path #
            ## Image path = ./images/index.ext ##
            # Get enclosure
            url = item['enclosure']['@url']
            logImage = url
            # Get extension
            ext = url.split('.')[-1]
            if ext == 'jpg':
                    logImage = url
                    imagesToDownload.append(url)
                    # Create folder images if not exists
                    if not os.path.exists('./images/'):
                        os.makedirs('./images/')
                    # Set filename index and ext
                    filename = f'./images/{indexXml}.{ext}'
                    path = doc.createElement('linkfoto')
                    path.appendChild(doc.createTextNode(filename))
                    # Close item #
                    item = doc.createElement('item')
                    item.appendChild(title)
                    item.appendChild(description)
                    item.appendChild(path)
                    channel.appendChild(item)
                    indexXml += 1
                    # Log title, description and image #
                    logging.info('Title: {} | Description: {} | Image: {}'.format(logTitle, logDescription, logImage))
    # Save feed.xml UTF8 #
    with open('feed.xml', 'w', encoding='utf-8') as f:
        f.write(doc.toprettyxml(indent='  ', encoding='utf-8').decode('utf-8'))
        # Log done time
        now = time.ctime(time.time())
        logging.info('Done time main: {}'.format(now))
        # Print done time
        # print(now)

async def downloader():
    global imagesToDownload
    logging.info('Start time downloader: {}'.format(time.ctime(time.time())))
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
        for index, url in enumerate(imagesToDownload):
            # Get extension
            ext = url.split('.')[-1]
            # Split ? on ext
            ext = ext.split('?')[0]
            if ext == 'jpg':
                # Set filename index and ext
                filename = f'./images/{index}.{ext}'
                # Download image
                async with session.get(url) as response:
                    content = await response.read()
                    with open(filename, 'wb') as f:
                        f.write(content)
                        # If filesize is > 1MB, compress image with PIL
                        if os.path.getsize(filename) > 1000000:
                            img = Image.open(filename)
                            img.save(filename, quality=20)                        
                        # Log done download #
                        logging.info('Downloaded {} from {}'.format(filename, url))
    # Log done time
    logging.info('Done time downloader: {}'.format(time.ctime(time.time())))


if __name__ == '__main__':
        main()
        asyncio.run(downloader())

