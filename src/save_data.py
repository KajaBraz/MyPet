from time import time
from src.pet import PetAttributes
from src.manage_time import step


def save(pet):
    with open('pet', 'w') as pet_file:
        pet_file.writelines(
            [str(time()), str(pet.bond), str(pet.food), str(pet.energy), str(pet.hygiene), str(pet.happiness),
             str(pet.poo)])


# def reopen(pet_file):
#     with open('pet', 'r') as pet_file:
#         metrics = pet_file.readlines()
#         pet = PetAttributes(metrics[1], metrics[2], metrics[3], metrics[4], metrics[5], metrics[6])
#         time_passed = time() - metrics[0]
#         pet = step(pet, time_passed)
#         return pet
