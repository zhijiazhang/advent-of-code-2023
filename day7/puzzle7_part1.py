import collections
import heapq

def calc_weight(hand, card_order):
    return [card_order.index(card) for card in hand]

def solve(filename: str) -> int:
    #1. group each hand based on type
    #2. sort each group
    #3. calc total 

    hands = {}
    groups = collections.defaultdict(list)
    card_order = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    hand_order = ["high", "one", "two", "three", "full", "four", "five"]
    total = 0

    with open(filename) as reader:
        for line in reader.readlines():
            hand, bid = line.split()
            hands[hand] = bid
            count = collections.Counter(hand)
            len_ = len(count)

            #five of a kind
            if len_ == 1:
                groups["five"].append(hand)
            
            #four of a kind or full house
            elif len_ == 2:
                if any(val == 4 for val in count.values()): groups["four"].append(hand)
                else: groups["full"].append(hand)

            #three of a kind or two pair
            elif len_ == 3:
                if any(val == 3 for val in count.values()): groups["three"].append(hand)
                else: groups["two"].append(hand)
                
            #one pair
            elif len_ == 4:
                groups["one"].append(hand)
            
            #high card
            else:
                groups["high"].append(hand)

    rank = 1

    for type in hand_order:
        if type not in groups: continue

        pq = [(calc_weight(hand, card_order), hand) for hand in groups[type]]
        heapq.heapify(pq)

        while(pq):
            curr_hand = heapq.heappop(pq)[1]
            total += int(hands[curr_hand]) * rank
            rank += 1

    return total