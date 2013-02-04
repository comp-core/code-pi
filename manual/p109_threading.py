# Example from Pi Educational Manual v1.0 P. 109
# Provided under a Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License

import threading
from urllib.request import urlopen
from xml.dom import minidom
import time

# extract weather details by grabbing tags from the RSS feed
# 'channel' contains all titles that contain weather heading text
def ExtractWeather(doc):
    for node in doc.getElementsByTagName('channel'):
        for title in node.getElementsByTagName('title'):
            print(title.firstChild.data)

class urlOpenThread(threading.Thread):
    def __init__(self, host):
        threading.Thread.__init__(self)
        self.host = host

    def run(self):
        # open the rss feed and then parse the result into a
        # web document - add this to end of the results list
        global results
        results.append(minidom.parse(urlopen(self.host)))

bbc_weather = "http://open.live.bbc.co.uk/weather/feeds/en/"
locations = ["2653941", "2655603", "2633352", "2653822", "2650752"]
forecast = "/3dayforecast.rss"

results = []
startingThreads = threading.activeCount()
start = time.time()

# create a thread for each url open and start it running
for location in locations:
    urlOpenThread(bbc_weather+location+forecast).start()

while threading.activeCount() > startingThreads:
    pass

print("Elapsed Time: %s" % (time.time() - start))

for webDoc in results:
    ExtractWeather(webDoc)
