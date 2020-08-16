from src.pet import PetAttributes
from src.activities import activities
from src.manage_time import step
from time import time


def prototype_game():
    pieseczek = PetAttributes()
    print("Your pet is born! Look if it's doing well")
    print(pieseczek)
    last_update = time()
    state = 'stand-by'

    while pieseczek.is_fine():
        print("\nWhat do you want to do with your pet? Choose one of the following:\nsleep\nfeed\nplay\nteach "
              "tricks\nwalk\nwash")
        print("If you don't want do anything, press ENTER")
        print("If you want to finish current action, type: stop")

        action = input().lower()
        input_time = time()
        if action in activities:
            if action == 'stand-by':
                state = 'stand-by'
                print("Your pet is in stand-by mode", "\n")
                pieseczek = step(pieseczek, input_time - last_update)
                last_update = time()
            elif action == 'stop':
                print(f"Your dog finished {state} and now is in stand-by mode", "\n")
                pieseczek = activities[state](pieseczek, input_time - last_update)
                state = 'stand-by'
                last_update = time()
            if state != action:
                pieseczek = activities[state](pieseczek, input_time - last_update)
                state = action
                print(f'Your dog is in {state} mode', "\n")
            elif state == action:
                pieseczek = activities[state](pieseczek, input_time - last_update)
                last_update = time()
            elif action == 'stop':
                print(f"Your dog finished {action} and now is in stand-by mode", "\n")
                pieseczek = activities[state](pieseczek, input_time - last_update)
                state = 'stand-by'
                last_update = time()
        else:
            print(f"Your pet is in {state} mode", "\n")
            pieseczek = activities[state](pieseczek, input_time - last_update)
            last_update = time()

        print(pieseczek)

    print("You've neglected your pet! It went away from you! Be more careful next time!")


if __name__ == "__main__":
    prototype_game()
