from unique_names_generator import get_random_name
from unique_names_generator.data import ADJECTIVES

choice = input("Would you like a manual name or auto generated name? (1/2)")
if choice == "1":
    first_name = input("What is the name that you would like to have in the band name?")
    output =  get_random_name(combo=[ADJECTIVES])+" "+first_name.capitalize()
elif choice == "2":
    output = get_random_name()
else: print("Please enter a valid choice.")

print("You can name your band as:",output)

