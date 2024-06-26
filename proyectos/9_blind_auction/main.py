from art import logo
import os

from art import logo
print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(biddin_record):
    highest_bid = 0
    winner = ''
    # bidden_record = {'Angela': 123, 'James': 321}
    for bidder in biddin_record:
        bid_amount = biddin_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f'The winner is {winner} whith a bid of ${highest_bid}')

while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input('What is your bid?: $'))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.")
    if should_continue == 'no':
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == 'yes':
        os.system('cls' if os.name == 'nt' else 'clear')
