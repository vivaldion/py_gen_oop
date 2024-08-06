import sys
from collections import Counter
from functools import reduce
cards = sys.stdin.readlines()
cards = Counter(map(lambda x: x.strip(), cards))
for_sell = reduce(lambda x, y: x+ y - 1 if y >= 2 else x + 0, cards.values(), 0)
print(for_sell)

