__author__ = 'konstantindmitriev'

import difflib


class HTMLComparison:

    def __init__(self):
        pass

    def compareTwoHTMLFiles(self, html1, html2):
        differ = difflib.Differ()
        difference = differ.compare(html1, html2)
        print(difference)