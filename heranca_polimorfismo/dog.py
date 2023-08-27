import animal

class Dog(animal.Animal):
    def __init__(self, name, birth, owner):
        super().__init__("Cachorro", name, birth)
        self.owner = owner

    # Imprime dados de cadastro do cachorro
    def get(self):
        registration_date_formatted = f"Data de Registro: {self.registration_date}"
        name_formatted = f"\nNome: {self.name}"
        race_formatted = f"\nRaça: {self.race}"
        birth_formatted = f"\nNascimento: {self.birth}"

        print(f"Dados da {self.name} ------")
        print(registration_date_formatted + name_formatted + \
              race_formatted + birth_formatted)


