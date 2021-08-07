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

    def __eq__(self, other):
        return (self.suit , self.rank) == (other.suit , other.rank)

    def __lt__(self , other):
        if self.suit == other.suit:
            return self.rank < other.rank
        return self.suit < other.suit

c1 = Card(3 , 13)
c2 = Card(2 , 10)

print(c1 ,'\n',c2 , '\n')

print(c1 == c2)
print(c1 != c2)
print(c1 < c2)
print(c1 > c2)