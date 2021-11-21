from art import logo
print(logo)

# Creating a condition to check if there are more bidders when the current bidder is bidding.
more_bidders = True

# Creating an empty dictionary to store the names and bids
name_bid = {}

while more_bidders:
    # Getting the name of the player
    name = input("What is your name?: ")

    # Getting the big amount from the player
    bid = int(input("What is your bid?: ₹"))

    # Storing the name and the bid in the dictionary named name_bid
    name_bid[name] = bid

    # Asking the user if there are more bidders
    are_there_more_bidders = input("Are there more bidders? Type 'yes' or 'no'.")

    # Creating an if and else statement to clear the console and also to check whether to continue the process of
    # asking for name and bid.
    # This clear function will not work in other IDE's. This will only work when you are call it in replit IDE.
    if are_there_more_bidders == "no":
        more_bidders = False

# Creating the highest_bid variable to store the highest bid value
highest_bid = 0

# Creating highest_bidder to store the highest bidder's name
highest_bidder = ""

# Creating a for loop to loop through all the keys in the dictionary
for thing in name_bid:
    # Creating a variable to_work_now to store the bid of the current bidder
    to_work_now = name_bid[thing]
    # Using if statement to check and update the highest bid and the bidder's name in the respective variables.
    if to_work_now > highest_bid:
        highest_bid += to_work_now
        highest_bidder = thing

# Printing the winner
print(f"The winner is {highest_bidder} with a bid of ₹{highest_bid}.")