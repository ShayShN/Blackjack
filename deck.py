import random

temp = {"2":2,
        "3":3,
        "4":4,
        "5":5,
        "6":6,
        "7":7,
        "8":8,
        "9":9,
        "10":10,
        "J":10,
        "Q":10,
        "K":10,
        "A":1,}
arr = ["H", "C", "D", "S"]

def build_standard_deck() -> list[dict]:
    package = []
    for i in arr:
        for v in temp:
            package.append({"rank": temp[v], "suite": i})
    return package



def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]:
    swaps = swaps
    while swaps > 0:
        index1 = random.randint(0, 51)
        index2 = random.randint(0, 51)
        if index1 == index2:
            continue
        card1 = deck[index1]
        card2 = deck[index2]
        if card1["rank"] == card2["rank"]:
            continue
        if card2["suite"] == "H":
            if int(card2["rank"]) % 5 != 0:
                continue
        if card2["suite"] == "C":
            if int(card2["rank"]) % 3 != 0:
                continue  
        if card2["suite"] == "D":
            if int(card2["rank"]) % 2 != 0:
                continue 
        if card2["suite"] == "S":
            if int(card2["rank"]) % 7 != 0:
                continue
        
        swaps -= 1
        deck[index1] , deck[index2] = deck[index2] , deck[index1]
        
    return deck


