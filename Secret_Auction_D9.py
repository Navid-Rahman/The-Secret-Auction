import os
clear = lambda: os.system('cls')
from art import logo

print(logo)

bid = {}

def maximum_bidder(bidding_record):
    max_bid = 0
    for bidder in bidding_record:
        bidding_amount = bidding_record[bidder]
        if bidding_amount>max_bid:
            max_bid = bidding_amount
            winner = bidder
    
    print(f"The winner is {winner} with a bid of ${max_bid}")


next = True
while next:
    name = input("What is your name?\n")
    bid_price = int(input("What is your bid?\n$"))
    bid[name] = bid_price
    
    next_bidder = input("Are there any other bidder? Type 'Yes' or 'No'\n").lower()
    if next_bidder == "no":
        next=False
        maximum_bidder(bid)
    elif next_bidder == "yes":
        clear()
        
    
# print(bid)
