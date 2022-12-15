import random

userName = "Black"
userPlanet = ['Deutron', 'Axton', 'Capricon', 'Galacticon']

name = input("Enter your name: ")
nameLength = len(name)
print("nameLength is " + str(nameLength))

if 2 < nameLength < 11:
  print(name + " is a valid username")
  planet = input("Choose your planet: ")
  userPlanet = ['Deutron', 'Axton', 'Capricon', 'Galacticon']

  if planet in userPlanet:
   print(planet + " is valid")
  
  

   numberInput = int(input("Guess a number between 1000 to 2500: "))
   randomNumber = random.randint(1000, 2500)
   print(str(randomNumber) + " is valid")

   if numberInput <= randomNumber:
     print("You lose")

   else: 
     print("You win")
  else: 
   print(planet + " is invalid! Choose between Deutron, Axton, Capricon, Galacticon")


else: 
  print("Username is invalid! Try a username between 3 and 10")




