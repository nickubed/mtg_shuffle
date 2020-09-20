import random

class MtgShuff:
    def __init__(self, count = 0, merged = []):
        self.count = count
        self.merged = merged
    def mtg_shuffle(self, ls):
        piles = []
        while self.count < 5:

            for _ in range(10 if len(ls) > 10 else len(ls)):
                piles.append([])
            while len(ls) > 0:
                for p in piles:
                    for _ in ls:
                        p.append(ls.pop(0))
                        break
                continue
            
            for p in piles:
                while len(p):
                    for _ in p:
                        self.merged.append(p.pop(random.randint(0,len(p)-1)))
                        break
                continue
            self.count += 1
            self.mtg_shuffle(self.merged)

        return self.merged

standard_deck = [{'Card': x} for x in range(60)]

shuff = MtgShuff()

print(shuff.mtg_shuffle(standard_deck))