print("The Love Calculator is calculating your score...")
name1 = input("What is your name? ") # What is your name?
name2 = input("What is your crushes name? ") # What is their name?
combined_names = name1 + name2
lower_caseNames = combined_names.lower()

t = lower_caseNames.count("t")
r = lower_caseNames.count("r")
u = lower_caseNames.count("u")
e = lower_caseNames.count("e")
true = t + r + u + e

l = lower_caseNames.count("l")
o = lower_caseNames.count("o")
v = lower_caseNames.count("v")
e = lower_caseNames.count("e")
love = l + o + v + e

true_love = int(str(true)+ str(love))

if true_love < 30:
  print(f"Your love score is {true_love}, you are not meant to be")
elif true_love < 60:
  print(f"Your love score is {true_love}, maybe in another lifetime")
elif true_love < 90:
  print(f"Your love score is {true_love}, you are meant to be")
elif true_love > 90:
  print(f"SOULMATES")

