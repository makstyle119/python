from Card import Card
import random

class Deck:
    def __init__(self):
        self.cards = []
        suits = ["hearts", "diamonds", "clubs", "spades"]
        ranks = [
            {"rank": "A", "value": 11},
            {"rank": "2", "value": 2},
            {"rank": "3", "value": 3},
            {"rank": "4", "value": 4},
            {"rank": "5", "value": 5},
            {"rank": "6", "value": 6},
            {"rank": "7", "value": 7},
            {"rank": "8", "value": 8},
            {"rank": "9", "value": 9},
            {"rank": "J", "value": 10},
            {"rank": "Q", "value": 10},
            {"rank": "K", "value": 10}
        ]
        self.create_cards(suits, ranks)

    def create_cards(self, suits, ranks):
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))  # Use a tuple instead of a list for better readability

    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal(self, number=1):
        card_dealt = []
        for _ in range(number):
            if len(self.cards) > 0:  # Check if there are cards left to deal
                card_dealt.append(self.cards.pop())
            else:
                break  # Exit if there are no cards left
        return card_dealt
