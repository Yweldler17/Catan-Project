DEVELOPMENT_CARD_NAMES = ["knight", "victory point",
                          "road building", "year of plenty", "monopoly"]


class DevCards:
    def __init__(self):
        self.cards = {}
        self.cards[0] = 14
        self.cards[1] = 5
        for i in range(2,5):
            self.cards[i] = 2

    def remove_from_bank(self, card):
        self.cards[card] -= 1

    def __str__(self):
        a = 'The bank has:\n'
        for i,j in self.cards.items():        
            a += str(j) + ' '
            a += DEVELOPMENT_CARD_NAMES[i]+ '\n'
        return a

        

print(DevCards())
