import collections
from random import choice
#自 Python 2.6 开始，namedtuple就加入到 Python 里，用以 构建只有少数属性但是没有方法的对象，比如数据库条目
Card = collections.namedtuple('Card',['card','suit'])
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
class FrenchDeck:
    """
    __init__:初始化纸牌
    __len__:初始化纸牌的张数
    __getitem__:打印这个纸牌是可迭代的
    """
    ranks = [str(n) for n in range(2,11)] + list('JQKA') #['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = 'spades diamonds clubs hearts'.split() #['spades', 'diamonds', 'clubs', 'hearts']

    def __init__(self):
        self._cards = [Card(rank,suit) for rank in self.ranks
                       for suit in self.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, index):
        return self._cards[index]



    def spades_high(card):
        rank_value = FrenchDeck.ranks.index(card.rank)
        return rank_value * len(suit_values) + suit_values[card.suit]


if __name__ == '__main__':
    #init接着用的都必须要有完整的对象才能使用。
    print(FrenchDeck.ranks)
    print(FrenchDeck.suits)
    print(Card('7', 'diamonds'))
    #__len__
    deck = FrenchDeck()
    print(len(deck))
    #__getitem__
    print(deck[-1])
    #正向/反向迭代
    for i in deck:
        print(i,end="")
    print()
    for i in reversed(deck):
        print(i,end="")
    #__init__
    print()
    print(choice(deck))
    print(choice(deck))
    print(choice(deck))
    #不同的方式找到迭代对象的数据string实现了__contains__方法
    print("1234567,ni".__contains__("1"))
    print("1234567,ni".find("6"))
    #可以迭代的都能用in方法
    print(Card('Q', 'hearts') in deck)


