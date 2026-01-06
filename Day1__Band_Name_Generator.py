from unique_names_generator import get_random_name
from unique_names_generator.data import ADJECTIVES
from names_generator import generate_name

choice = input("Would you like a manual name or auto generated name? (1/2)\n")
if choice == "1":
    first_name = input("What is the name that you would like to have in the band name?\n")
    for i in range(10):
        output =  get_random_name(combo=[ADJECTIVES])+" "+first_name.capitalize()
        print(output)
elif choice == "2":
    for i in range(10):
        output = generate_name(style='capital')
        print(output)
else: print("Please enter a valid choice.")

