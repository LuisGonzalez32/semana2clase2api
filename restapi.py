  
import requests


class MtgRestApi:
    def __init__(self):
        self.base = "https://api.magicthegathering.io"
        self.endpoint = "/v1/cards"
        self.params = {"set": "ONS", "supertypes": "Legendary"}

    def getMtgCards(self):
        response = requests.get(self.base + self.endpoint, params=self.params)
        cards = []
        if response.status_code == 200:
            cardJson = response.json()
            cards = cardJson["cards"]
        return cards