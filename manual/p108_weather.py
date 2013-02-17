# Example from Pi Educational Manual v1.0 P. 106
# Provided under a Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License

from urllib.request import urlopen
from xml.dom import minidom
import time

# extract weather details by grabbing tags from the RSS feed
# 'channel' contains all titles that contain weather heading text
def ExtractWeather(doc):
    for node in doc.getElementsByTagName('channel'):
        for title in node.getElementsByTagName('title'):
            print(title.firstChild.data)

results = []

bbc_weather = "http://open.live.bbc.co.uk/weather/feeds/en/"
locations = ["2653941", "2655603", "2633352", "2653822", "2650752"]
forecast = "/3dayforecast.rss"

start = time.time()

for location in locations:
    # open the rss feed and parse the result into a web document
	# and add the doc to the end of the list
    results.append(minidom.parse(urlopen(bbc_weather+location+forecast)))

elapsedTime = (time.time() - start))

for webDoc in results:
    ExtractWeather(webDoc)

print("Elapsed Time: %s" % elapsedTime)
