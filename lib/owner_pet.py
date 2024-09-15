class Pet:
    PET_TYPES = ['dog', 'cat','bird', 'exotic', 'reptile', 'rodent']

    all = []
    def __init__(self, name, species, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
         raise ValueError(f"Invalid pet type: {pet_type}. Must be one of {Pet.PET_TYPES}.")
        
        self.name = name
        self.pet_type = pet_type
        self.owner = owner

    
        if owner:
            owner.add_pet(self)
        Pet.all.append(self)


    pass

class Owner:
    def __init__(self, name):
        self.name = name
        self.pets = []

    def pets(self, pet):
        return  self.pets

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError("Only Pet instances can be added.")
        
        pet.owner = self  
        self._pets.append(pet)  

    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet.name)