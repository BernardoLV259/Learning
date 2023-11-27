import math
def paint_calc(height, width, cover):
  number_of_cans = math.ceil((height * width)/cover)
  print(f"You'll need {number_of_cans} cans of paint.")

test_h = int(input("Enter height of wall (m): ")) 
test_w = int(input("Enter width of wall (m): ")) 
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
