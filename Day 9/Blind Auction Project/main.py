# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
from art import logo

print(logo)
print("Welcome to the secret auction program")
bid_data = {}
flag = True # Ture if one or more bidders are present
while flag:
    name = input("What is your name? : ")
    bid_data[name] = int(input("What is your bid? : "))
    add_bidder = input("Are there any other bidders? Type 'yes' or 'no' : ").lower()
    # assert add_bidder == 'yes' or add_bidder == 'no', "Type correctly as requested."
    if add_bidder == "no":
        flag = False
    print("\n"*100)

max_bid = 0
index = 0
for key, value in bid_data.items():
    if value >= max_bid:
        max_bid = value
        index = key

print(f"The winner is {index} with a bid of {max_bid} ")

index, max_bid = max(bid_data.items(), key= lambda items: (items[1], items[0]))
print(f"The winner is {index} with a bid of {max_bid} ")






