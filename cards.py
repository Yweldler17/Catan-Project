
RESOURCE_NAMES = [ "brick", "ore", "hay", "wood", "sheep"]
class Res_cards:
    def __init__(self):
        self.cards = {}
        for i in RESOURCE_NAMES:
            self.cards[i] = [0] * 19
        

    def __str__(self):
        a = 'The card bank has:\n'
        a += '{} ore\n'.format(str(len(self.cards['ore'])))
        a += '{} brick\n'.format(str(len(self.cards['brick'])))
        a += '{} hay\n'.format(str(len(self.cards['hay'])))
        a += '{} wood\n'.format(str(len(self.cards['wood'])))
        a += '{} sheep\n'.format(str(len(self.cards['sheep'])))
        return a

print(Res_cards())
