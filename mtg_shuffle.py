import random
count = 0
merged = []
def mtg_shuffle(ls):
    global count
    global merged
    piles = []
    while count < 5:

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
                    merged.append(p.pop(random.randint(0,len(p)-1)))
                    break
            continue
        count += 1
        mtg_shuffle(merged)

    return merged

standard_deck = [{'Card': x} for x in range(60)]

print(mtg_shuffle(standard_deck))