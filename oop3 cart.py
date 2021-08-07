# hearts            0
# diamonds          1
# spades            2
# clubs             3

# 1,2,3,4,5,6,7,8,9,10,Jack,Queen,King
                    #   11   12    13
# suit rank

class Card:
    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank  = rank

    def __str__(self):
        suit_list = ['Hearts' , 'Diamonds' , 'Spades' , 'Clubs']
        rank_list = [0 , 'Ace','2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        return (rank_list[self.rank]+' of '+suit_list[self.suit])


cards = Card(3 , 13)
print(cards)