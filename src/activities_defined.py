from src.pet import PetAttributes
from src.attributes_coeficients import food_decrement, energy_decrement, hygiene_decrement, \
    poo_decrement, bond_increment, food_increment, energy_increment, hygiene_increment, \
    happiness_increment, poo_increment


def copy_attributes(pet: PetAttributes) -> PetAttributes:
    clone = PetAttributes(pet.bond, pet.food, pet.energy, pet.hygiene, pet.happiness, pet.poo)
    return clone


def sleep(pet):
    updated_pet = copy_attributes(pet)
    updated_pet.energy += energy_increment
    updated_pet.food += food_decrement
    updated_pet.hygiene += hygiene_decrement
    return updated_pet


def feed(pet):
    updated_pet = copy_attributes(pet)
    updated_pet.bond += bond_increment
    updated_pet.food += food_increment
    updated_pet.poo += poo_increment
    return updated_pet


def play(pet):
    updated_pet = copy_attributes(pet)
    updated_pet.bond += bond_increment
    updated_pet.energy += energy_decrement
    updated_pet.happiness += happiness_increment
    return updated_pet


def teach_tricks(pet):
    updated_pet = copy_attributes(pet)
    updated_pet.bond += bond_increment
    updated_pet.energy += energy_decrement
    updated_pet.happiness += happiness_increment
    return updated_pet


def walk(pet):
    updated_pet = copy_attributes(pet)
    updated_pet.bond += bond_increment
    updated_pet.energy += energy_decrement
    updated_pet.happiness += poo_decrement
    return updated_pet


def wash(pet):
    updated_pet = copy_attributes(pet)
    updated_pet.bond += bond_increment
    updated_pet.hygiene += hygiene_increment
    return updated_pet


def meet_friend(pet1, pet2):
    pass


def dream(pet):
    pass
