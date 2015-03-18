__author__ = 'konstantindmitriev'

import requests
import json

class CollectData:
    # Russian providers do not block every pages from the register (idk why).
    # This is the list of manually selected pages that cannot be accessed from russian VPN server (IPVanish)
    # but they are accessible from servers outside of Russia
    listOfDefinitelyBlockedPages = [{'url': 'http://leonwolf.livejournal.com', 'ip': '208.93.0.190'},
                                    {'url': 'http://navalny.livejournal.com', 'ip': '208.93.0.190'}]

    def __init__(self):
        # Init Connection Class
        # self.connection = Connection()
        # Init SaveData Class
        pass

    # access multiple webpages from a single country
    def collectMultipleWebpagesFromASingleCountry(self, countryID, numberOfWebpagesToAccess, flagUseManuallySelectedListInsteadOfAntiZapret):
        # open the connection using countryID

        # listOfBlockedWebsites = []
        if (flagUseManuallySelectedListInsteadOfAntiZapret):
            listOfBlockedWebsites = self.listOfDefinitelyBlockedPages
        else:
            requestAListOfBlockedWebsites = requests.get('http://api.antizapret.info/all.php?type=json')
            # decode the received data
            listOfBlockedWebsites = json.loads(requestAListOfBlockedWebsites.text)['register']
        # go through websites in the list
        for blockedWebsite in listOfBlockedWebsites[:numberOfWebpagesToAccess]:  # first n results
            blockedURL = blockedWebsite['url']
            htmlCodeOfThePage = requests.get(blockedURL, timeout = 8).text # timeout = 8 seconds

            # print(blockedURL)
            # print(htmlCodeOfThePage)

            # save html code of the page (input: blockedURL, htmlCodeOfThePage)

        # close the connection

    # access a single webpage from multiple countries
    def collectOneWebpageFromMultipleCoutries(self, listOfCountryIDs, url):
        for countryID in listOfCountryIDs:
            # open the connection using countryID

            htmlCodeOfThePage = requests.get(url).text

            # save html code of the page (input: url, htmlCodeOfThePage)

            # close the connection
        pass

# # Examples:
# collectDataHandler = CollectData()
# collectDataHandler.collectMultipleWebpagesFromASingleCountry(1, 2, 1)