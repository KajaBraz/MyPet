from time import time
from src.pet import PetAttributes
from src.manage_time import step


def save(pet):
    with open('pet', 'w') as pet_file:
        pet_file.write('\n'.join(
            [str(time()), str(pet.bond), str(pet.food), str(pet.energy), str(pet.hygiene), str(pet.happiness),
             str(pet.poo)]))


def reopen(pet_file_path):
    pet_file = open(pet_file_path, 'r')
    metrics = pet_file.readlines()
    pet = PetAttributes(float(metrics[1]), float(metrics[2]), float(metrics[3]), float(metrics[4]), float(metrics[5]),
                        float(metrics[6]))
    time_passed = time() - float(metrics[0])
    pet = step(pet, time_passed)
    return pet
