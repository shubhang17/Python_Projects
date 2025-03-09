import art

# TODO-1: Ask the user for input


print(art.logo)

# TODO-2: Save data into dictionary {name: price}


# TODO-3: Whether if new bids need to be added

def find_highest_bidder(Bidding_Dictionary):
    winner = ""
    highest_bid = 0
    for bidder in Bidding_Dictionary:
        bid_amount = Bidding_Dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The Winner is {winner} with a bid of ${highest_bid}")

Bid_Dictionary={}
continue_bidding = True
while continue_bidding:
    name = input("Please Enter Your Name: ")
    Bid = int(input("Please Enter Your Bid: $ "))
    Bid_Dictionary[name] = Bid
    should_continue = input("Are there any other Bidders? Type 'Yes' or 'No'. \n").lower()
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(Bid_Dictionary)
    elif should_continue == "yes":
        print("\n" * 20)





