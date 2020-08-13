from pet import PetAttributes
from activities import activities
from manage_time import step
from time import time


def prototype_game():
    pieseczek = PetAttributes()
    print("Your pet is born! Look if it's doing well")
    print(pieseczek)
    while pieseczek.is_fine():
        print("\nWhat do you want to do with your pet? Choose one of the following:\nsleep\nfeed\nplay\nteach "
              "tricks\nwalk\nwash")
        print("If you don't want do anything, press ENTER")
        start_time = time()

        action = input()
        if action.lower() in activities:
            print('Updating ', action)
            end_time = time()
            pieseczek = step(pieseczek, end_time - start_time)
            pieseczek = activities[action](pieseczek)
        else:
            print('Your dog is in stand-by mode')
            end_time = time()
            pieseczek = step(pieseczek, end_time - start_time)

        print(pieseczek)

    print("You've neglected your pet! It went away from you! Be more careful next time!")


if __name__ == "__main__":
    prototype_game()
