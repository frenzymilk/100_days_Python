import os
from art import logo

print(logo)

auction_log = dict()

def set_bid():
	name = input("What is your name? ")
	bid = int(input("What is your bid? "))
	auction_log{name:bid}


continue_bid = True
while continue_bid:
	set_bid()
	user_input = input("Are there any other bidders? Type 'yes' or 'no'. \n")
	if user_input == "no":
		continue_bid = False
	elif user_input == "yes":
		os.system("clear")

max_val = 0
max_name = ""
for key in auction_log:
	if auction_log[key] > max_val:
		max_val = auction_log[key]
		max_name = key

print(f"The winner is {max_name} with a bid of ${max_val}")