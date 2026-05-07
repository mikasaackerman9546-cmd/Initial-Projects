import random

while True:
 choice = input("Roll your dice(y/n):")
 if choice == "y" or choice == "Y":
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    print(die1 ,die2)
 elif choice == "n":
    print("Thanks for playing.")
 else:
   print("Invalid Choice!")
