from src.pet import PetAttributes
from src.activities import activities
from src.manage_time import step
from src.save_data import save, reopen
from time import time

def prototype_game(saved_pet=None):
    if saved_pet is None:
        my_pet = PetAttributes()
        print("Your pet is born! Let's check if it's doing well")

    else:
        my_pet = reopen(saved_pet)

    print(my_pet)
    last_update = time()
    state = 'stand-by'

    while my_pet.is_fine():
        print(f"\nWhat do you want to do with your pet? Choose one of the following:\nsleep\nfeed\nplay\nteach "
              "tricks\nwalk\nwash")
        print("If you want to finish current action, type: stop\n")

        action = input()
        input_time = time()
        if action in activities:
            if action == 'stand-by':
                state = 'stand-by'
                print("Your pet is in stand-by mode", "\n")
                my_pet = step(my_pet, input_time - last_update)
                last_update = time()
            elif action == 'stop':
                print(f"Your dog finished {state.upper()} and now is in stand-by mode", "\n")
                my_pet = activities[state](my_pet, input_time - last_update)
                state = 'stand-by'
                last_update = time()
            elif action == 'END':
                print("Last updating before saving the game")
                my_pet = activities[state](my_pet, input_time - last_update)
                save(my_pet)
                print(my_pet)
                break
            else:
                state = action
                print(f'Your dog is in {state.upper()} mode', "\n")
                my_pet = activities[state](my_pet, input_time - last_update)
                last_update = time()
        else:
            print(f"Invalid action. Your pet is in {state.upper()} mode", "\n")
            my_pet = activities[state](my_pet, input_time - last_update)
            last_update = time()

        print(my_pet)
    if not my_pet.is_fine():
        print("You've neglected your pet! It went away from you! Be more careful next time!")


if __name__ == "__main__":
    prototype_game('pet')
