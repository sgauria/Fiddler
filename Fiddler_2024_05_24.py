# This Week’s Fiddler

# You’re playing a modified version of blackjack, where the deck consists of exactly 10 cards numbered 1 through 10. 
# Unlike traditional blackjack, in which the ace can count as 1 or 11, the 1 here always has a value of 1.

# You shuffle the deck so the order of the cards is completely random, after which you draw one card at a time. 
# You keep drawing until the sum of your drawn cards is at least 21. If the sum is exactly 21, you win! 
# But if the sum is greater than 21, you “bust,” or lose. 

# What are your chances of winning, that is, of drawing a sum that is exactly 21?

# This Week’s Extra Credit

# Playing for 21 or bust is a risky strategy. From this moment on, you decide to be risk averse.

# You’re playing the same modified version of blackjack again, but this time, whenever there’s even the slightest chance 
# you could bust on the next card, you quit the round and start over. 
# On average, how many rounds should you expect to start until you finally win?

import itertools

N = 10 # number of cards
W = 21 # win value
cards = list(range(1,N+1))
print(cards)

M = 0 # max list size to consider
while(sum(cards[0:M]) < W):
    M += 1
print(M)

def find_outcome_of_sequence(l, extra_credit=0):
    """ Return W for Win(21), B for Bust, or Q for quit"""
    sum = 0
    for i in range(len(l)):
        x = l[i]
        sum += x
        if (extra_credit == 0):
            if (sum == W):
                return 'W'
        if (extra_credit == 1):
            if (sum < W): 
                max_next_sum = (sum + max(l[i+1:]))
                if (max_next_sum > W):
                    return 'Q'
            if (sum == W):
                return 'W'
        if (sum > W):
            return 'B'

assert(find_outcome_of_sequence([1,2,3,4,5,6,7,8,9,10],0) == 'W')
assert(find_outcome_of_sequence([1,2,3,4,5,7,6,8,9,10],0) == 'B')
assert(find_outcome_of_sequence([6,7,8,9,10,1,2,3,4,5],0) == 'W')
assert(find_outcome_of_sequence([6,8,9,1,2,3,4,5,7,10],0) == 'B')
assert(find_outcome_of_sequence([1,2,3,4,5,6,7,8,9,10],1) == 'Q')
assert(find_outcome_of_sequence([1,2,3,4,5,7,6,8,9,10],1) == 'Q')
assert(find_outcome_of_sequence([2,10,9,6,7,8,1,3,4,5],1) == 'W')
assert(find_outcome_of_sequence([2,9,10,6,7,8,1,3,4,5],1) == 'W')

print("Fiddler:")
outcomes = { 'W' : 0, 'B' : 0, 'Q' : 0, 'T' : 0}
for deck in itertools.permutations(cards, r=M):
    oc = find_outcome_of_sequence(deck, extra_credit=0)
    outcomes[oc] += 1
    outcomes['T'] += 1
print(outcomes)
w = (outcomes['W'] / outcomes['T'])
print(f"Chance of winning = {w}")


print("\n\nExtra Credit:")
outcomes = { 'W' : 0, 'B' : 0, 'Q' : 0, 'T' : 0}
for deck in itertools.permutations(cards):
    oc = find_outcome_of_sequence(deck, extra_credit=1)
    outcomes[oc] += 1
    outcomes['T'] += 1
print(outcomes)

# We have probabilities w and q of winning and quitting respectively.
# Expected number of rounds
# = w.1 + q.w.2 + q^2.w.3 ...
# = w (1 + 2q + 3q^2 ... )
# = w ((1 + q + q^2 ...) + (q + q^2 + ... ) + (q^2 + q^3 + ... ) + ...)
# = w ((1/1-q) + (q/1-q) + ...)
# = w/(1-q)^2

w = (outcomes['W'] / outcomes['T'])
q = (outcomes['Q'] / outcomes['T'])
E_num_rounds = w / ((1-q)**2)
print(f"Expected number of rounds = {w} / ((1 - {q}) ** 2)= {E_num_rounds}")


