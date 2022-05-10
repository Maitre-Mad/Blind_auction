from replit import clear
import art
#HINT: You can call clear() to clear the output in the console.
print(art.logo)
print("Welcome to the secret aution program. ")
bid_log={}
bidder=True

while bidder:
  name=input("What is your name?: " )
  bid=int(input("What's your bid: $"))
  bid_log[name]=bid
  end_act=input("Is there more bidder ? Yes or No:  ").lower()
  clear()
  if end_act=="no":
    max_bid=max(bid_log,key=bid_log.get)
    print(f"The winner is {max_bid} with {bid_log[max_bid]}")
    bidder=False
  