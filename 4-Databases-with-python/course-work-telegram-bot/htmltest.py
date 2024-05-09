import requests

from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.result = []

    def handle_data(self, data):
        self.result.append(data)

    def get_data(self):
        return ''.join(self.result)

parser = MyHTMLParser()
with open('y.html') as f:
    f.seek(0)
    t = f.read()
    print(len(t))
    parser.feed(t)
print(parser.get_data())
