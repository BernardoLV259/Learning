print("Welcome to the BMI Calculator\n")
height = input("What is your height in meters? ")

weight = input("What is your height in kg? ")

weight = float(weight)
height = float(height)
bodymass = (weight)/(height**2)
print(int(bodymass))