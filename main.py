userName = "Black"
userPlanet = ['Deutron', 'Axton', 'Capricon', 'Galacticon']

name = input("Enter your name: ")

if len(name) >= 3 & len(name) <= 10:
  print(name + " is a valid username")

else: print("Username is invalid! Try a username between 3 and 10")