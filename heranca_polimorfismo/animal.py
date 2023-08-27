from datetime import datetime

class Animal():
    def __init__(self, race, name, birth):
        self.registration_date = datetime.now()
        self.race = race
        self.name = name
        self.birth = birth
        print("\nNovo animal de estimação cadastrado!\n")

    def calculate_age(self):
        age = datetime.now() - self.birth
        print(f"Idade: {age}")