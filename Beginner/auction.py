import os

who_bid_what = {}

def winner():
    winner = ""
    winning_bid = 0
    for i in who_bid_what:
        bid_amount = who_bid_what[i]
        if bid_amount > winning_bid:
            winning_bid = bid_amount
            winner = i 
    print(f"The winner is {winner} at ${winning_bid}")

initialize = True
while initialize:
    name = input("What is your name?\n")
    bid = int(input("How much do you want to bid?\n$"))
    who_bid_what.update({name:bid})
    bid_again = input("Anyone else want to bid 'yes' or 'no'?\n")
    if bid_again == 'yes':
        os.system('clear')
    else:
        initialize = False
        winner()

