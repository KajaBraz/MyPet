from src.pet import PetAttributes
from src.attributes_coeficients import food_decrement, energy_decrement, hygiene_decrement, \
    poo_decrement, bond_increment, food_increment, energy_increment, hygiene_increment, \
    happiness_increment, poo_increment

time_cons = 0.01


def copy_attributes(pet: PetAttributes) -> PetAttributes:
    clone = PetAttributes(pet.bond, pet.food, pet.energy, pet.hygiene, pet.happiness, pet.poo)
    return clone


def sleep(pet, delta=1):
    updated_pet = copy_attributes(pet)
    updated_pet.energy += energy_increment * delta * time_cons
    updated_pet.food += food_decrement * delta * time_cons
    updated_pet.hygiene += hygiene_decrement * delta * time_cons
    return updated_pet


def feed(pet, delta=1):
    updated_pet = copy_attributes(pet)
    updated_pet.bond += bond_increment * delta * time_cons
    updated_pet.food += food_increment * delta * time_cons
    updated_pet.poo += poo_increment * delta * time_cons
    return updated_pet


def play(pet, delta=1):
    updated_pet = copy_attributes(pet)
    updated_pet.bond += bond_increment * delta * time_cons
    updated_pet.energy += energy_decrement * delta * time_cons
    updated_pet.happiness += happiness_increment * delta * time_cons
    return updated_pet


def teach_tricks(pet, delta=1):
    updated_pet = copy_attributes(pet)
    updated_pet.bond += bond_increment * delta * time_cons
    updated_pet.energy += energy_decrement * delta * time_cons
    updated_pet.happiness += happiness_increment * delta * time_cons
    return updated_pet


def walk(pet, delta=1):
    updated_pet = copy_attributes(pet)
    updated_pet.bond += bond_increment * delta * time_cons
    updated_pet.energy += energy_decrement * delta * time_cons
    updated_pet.happiness += poo_decrement * delta * time_cons
    return updated_pet


def wash(pet, delta=1):
    updated_pet = copy_attributes(pet)
    updated_pet.bond += bond_increment * delta * time_cons
    updated_pet.hygiene += hygiene_increment * delta * time_cons
    return updated_pet


def meet_friend(pet1, pet2):
    pass


def dream(pet):
    pass


def get_ill(pet):
    pass
