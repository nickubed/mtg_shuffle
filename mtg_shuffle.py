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
        
        print(piles)
        for p in piles:
            while len(p):
                for _ in p:
                    merged.append(p.pop(random.randint(0,len(p)-1)))
                    break
            continue
        count += 1
        mtg_shuffle(merged)

    return merged


print(mtg_shuffle([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]))