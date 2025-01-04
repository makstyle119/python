class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self): # this will overwrite print functions
        return (f"{self.rank['rank']} of {self.suit}")
