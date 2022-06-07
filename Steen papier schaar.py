import random
print("welkom bij steen papier schaar lizard spock")

while True:
  print("Maak je keuze: ", end=" ")
  guess = str(input())
  guess = guess.lower()
  choices = ["steen", "papier", "schaar","lizard", "spock"]
  computer_keuze = random.choice(choices)
  print ("Jij koos voor",guess)
  print ("De computer koos voor", computer_keuze)
  if guess in choices:
     if guess == computer_keuze:
         print("het is gelijk spel, als je het mij vraagt hebben jullie beide verloren")
     elif guess == "steen":
         if computer_keuze == "schaar":
             print("gefeliciteerd je bent slimmer dan een computer wow")
         elif computer_keuze == "lizard":
             print("gefeliciteerd je bent slimmer dan een computer wow")
         elif computer_keuze == "papier":
             print("wow je hebt verloren 40% kans dat je niet verliest en dat kun je niet wow")
         elif computer_keuze == "spock":
             print("wow je hebt verloren 40% kans dat je niet verliest en dat kun je niet wow")
     elif guess == "papier":
         if computer_keuze == "steen":
             print("gefeliciteerd je hebt kunnen winnen had dit eerlijk gezegd niet van je verwacht")
         elif computer_keuze == "spock":
             print("gefeliciteerd je hebt kunnen winnen had dit eerlijk gezegd niet van je verwacht")
         elif computer_keuze == "schaar":
             print(" verloren")                 #edit text
         elif computer_keuze == "lizard":
             print(" verloren")                 #edit text
     elif guess == "schaar":
        if computer_keuze == "papier":
             print("gelfeliciteerd op een of andere manier heb je gewonnen knap hoor")
        elif computer_keuze == "lizard":
             print("gelfeliciteerd op een of andere manier heb je gewonnen knap hoor")
        elif computer_keuze == "steen":
             print(" verloren ")                #edit text
        elif computer_keuze == "spock":
             print(" verloren ")                #edit text
     elif guess == "lizard":
        if computer_keuze == "papier":
           print("eindelijk na jaren heb je gewonnen")
        elif computer_keuze == "spock":
           print("eindelijk na jaren heb je gewonnen")
        elif computer_keuze == "steen":
            print("weer eens verloren ik zie je echt vaak verliezen of niet soms")
        elif computer_keuze == "schaar":
            print("weer eens verloren ik zie je echt vaak verliezen of niet soms")
     elif guess == "spock":
        if computer_keuze == "papier":
            print(" verloren ")             #edit text
        elif computer_keuze == "lizard":
            print(" verloren ")             #edit text
        elif computer_keuze == "steen":
            print(" gewonnen  ")            #edit text
        elif computer_keuze == "schaar":
            print("gewonnen ")              #edit text
     print("")
  else:
      print("probeer dit maar opniew")                             #edit text
  verder_spelen = input("Wil je verder spelen (J/N)?")
  if verder_spelen != "J" and verder_spelen != "N":
    print("probeer dat maar opnieuw :[")  # edit text
  elif verder_spelen == "N" or "n":
   verder_spelen = False
     break
