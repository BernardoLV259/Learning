logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''#HINT: You can call clear() to clear the output in the console.
print(logo)

bidding_dictionary = {}
#bidding_dictionary = {Angel: 2, Bernardo, 300}

def auction_bidding(get_name="No one",get_bid=0):
  name = input("What is your name? ")
  bid = input("What is your bid? $")

  bidding_dictionary[name] = bid
  continuation = input("Are there any other bidders? Type 'yes' or 'no' ")
  
  if continuation == "yes":
    
    auction_bidding()
    
  elif continuation == "no":
    highest_bid = 0
    for name in bidding_dictionary:
      current_bid = int(bidding_dictionary[name])

      if current_bid > highest_bid:
        highest_bid = current_bid
        winner = name

    print(f"The Winner is {winner} with a bid of ${highest_bid}")

auction_bidding()













