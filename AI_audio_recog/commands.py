import os
import subprocess
from bs4 import BeautifulSoup
from get_answers import Fetcher


class Commander:
    def __init__(self):
        self.confirm = ["yes", "affirmative", "si", "sure", "afirmativo",
                        "do it", "yeah", "confirm", "confirmar"]
        self.cancel = ["no", "negative", "do not", "don't", "cancel", "wait"]

    def discover(self, text):
        if "what" in text and "your name" in text:
            if "my" in text:
                self.respond("You havent told me your name yet")
            else:
                self.respond("My name is PyCommander, How are you?")
        else:
            f = Fetcher("www.google.com/search?q=" + text)
            answer = f.lookup()
            self.respond(answer)

        if "open" or "lauch" in text:
            app = text.split(" ", 1)[-1]
            os.system("open -a" + app + ".app")

    def respond(self, response):
        print(response)
        subprocess.call("say " + response, shell=True)
