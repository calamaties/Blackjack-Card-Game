from cards import *

class player:

    def __init__(self, name, dealer="NULL", userRight=False):
        self.name = name
        self.dealer = dealer
        self.onHand = []
        self.totalOnHand = 0
        self.userRight = userRight
        self.cardBurst = False
        self.winner = "NULL"
        self.money = 0
        self.bet = 0

    def drawCard(self, deck):
        drawnCard = deck.pop(0)
        self.onHand.append(drawnCard)
        cardNum = int(cards.numbersRep['%s' % drawnCard[0]])
        self.totalOnHand += cardNum

        if self.totalOnHand > 21:
            self.totalOnHandAce11 = self.totalOnHand
            for m in self.onHand:
                if m[0] == "A":
                    cards.numbersRep['A'] = 1
            self.getTotalOnHand()

    def getTotalOnHand(self):
        totalOnHand = 0
        for i in self.onHand:
            totalOnHand += int(cards.numbersRep["%s" % i[0]])
            self.totalOnHand = totalOnHand
        cards.numbersRep['A'] = 11