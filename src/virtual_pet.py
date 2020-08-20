from src.pet import PetAttributes
from src.activities import activities
from src.manage_time import step
from src.save_data import save, reopen
from time import time


def prototype_game(pieseczek=None):
    if pieseczek is None:
        pieseczek = PetAttributes()
        print("Your pet is born! Look if it's doing well")

    print(pieseczek)
    last_update = time()
    state = 'stand-by'

    while pieseczek.is_fine():
        print("\nWhat do you want to do with your pet? Choose one of the following:\nsleep\nfeed\nplay\nteach "
              "tricks\nwalk\nwash")
        print("If you want to finish current action, type: stop\n")

        action = input()
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
            elif action == 'END':
                print("Last updating before saving the game")
                pieseczek = activities[state](pieseczek, input_time - last_update)
                save(pieseczek)
                print(pieseczek)
                break
            else:
                state = action
                print(f'Your dog is in {state} mode', "\n")
                pieseczek = activities[state](pieseczek, input_time - last_update)
                last_update = time()
        else:
            print(f"Invalid action. Your pet is in {state} mode", "\n")
            pieseczek = activities[state](pieseczek, input_time - last_update)
            last_update = time()

        print(pieseczek)

    # print("You've neglected your pet! It went away from you! Be more careful next time!")

    def continue_game(saved_game):
        pet = reopen(saved_game)
        print("You're back! Let's take a look how your pet is doing:")
        prototype_game(pet)


if __name__ == "__main__":
    prototype_game()
