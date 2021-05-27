
RESOURCE_NAMES = ["brick", "ore", "hay", "wood", "sheep"]


class Res_cards:
    def __init__(self):
        self.cards = {}
        for i in RESOURCE_NAMES:
            self.cards[i] = 19

    def add_to_bank(self, card):
        self.cards[card] += 1

    def remove_from_bank(self, card):
        self.cards[card] -= 1

    def __str__(self):
        a = 'The card bank has:\n'
        a += '{} ore\n'.format(str(self.cards['ore']))
        a += '{} brick\n'.format(str(self.cards['brick']))
        a += '{} hay\n'.format(str(self.cards['hay']))
        a += '{} wood\n'.format(str(self.cards['wood']))
        a += '{} sheep\n'.format(str(self.cards['sheep']))
        return a


print(Res_cards())
