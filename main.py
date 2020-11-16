from replit import clear
from  art import logo

print(logo)
print('''
''')

participants = dict()
auction = True

while auction:
  bidder = input("Enter your name? ")
  bid = int(input("Enter your bid amount: $"))
  participants[bidder] = bid
  print("")
  check_for_bidders = True
  while check_for_bidders:

    more_bidders = input("Are there any more bidder? (y/n) ").lower()
    if more_bidders == "y": 
      clear()
      check_for_bidders = False

    elif more_bidders == "n": 
      auction = False
      check_for_bidders = False
    else:
      print("Bad input! Please type 'y' or 'n' for your answer.")

# Auction participants:
print("")
print("Auction participants:")
for k, v in participants.items():
  print(f"  {k}, Bid amount: ${v}")

highest_bid = 0
winner = ""

for k, v in participants.items():
  if v > highest_bid:
    highest_bid = v
    winner = k
print("")
print(f"{winner} is the highest bidder with amount ${highest_bid} and is the auction winner.")



