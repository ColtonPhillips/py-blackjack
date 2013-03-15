import dialog

class Card:
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']   
    def __init__(self):
        # Whatever. Default to this.
        self.value = 0
        self.suit = suits[1]
        
    @staticmethod
    def random_card():
        import random
        card = Card()
        card.value = random.randint(0,13)
        card.suit = Card.suits[random.randint(0,3)]
        return card

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(52):
            self.cards.append(Card.random_card())
            print card.value

    def deal_card(self):
        pass

class Hand:
    def __init__(self):
        pass

def game_loop():
    print dialog.TABLE_INTRO

    active_game = True
    while active_game: 
        deck = Deck()
        active_game = False

def main():
    print dialog.PREAMBLE
    raw_input("Press Enter Key to play.")
    game_loop()
    print dialog.EPILOGUE

if __name__ == "__main__":
    main()