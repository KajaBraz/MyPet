from src.activities_defined import copy_attributes, sleep, feed, play, teach_tricks, walk, wash
from src.attributes_coeficients import bond_decrement, food_decrement, energy_decrement, hygiene_decrement, \
    happiness_decrement, poo_increment


def step(pet, delta=1):
    """Function that updates the pet's attributes, taking into consideration the time passed (default time passed -
    delta - is one step). It returns a new object. """
    time_cons = 0.001
    updated_pet = copy_attributes(pet)
    updated_pet.bond += bond_decrement * delta * time_cons
    updated_pet.food += food_decrement * delta * time_cons
    updated_pet.energy += energy_decrement * delta * time_cons
    updated_pet.hygiene += hygiene_decrement * delta * time_cons
    updated_pet.happiness += happiness_decrement * delta * time_cons
    updated_pet.poo += poo_increment * delta * time_cons
    return updated_pet


def stop_action(pet, action, delta):
    action(pet, delta)
