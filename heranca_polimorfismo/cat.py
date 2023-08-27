from animal import Animal

class Cat(Animal):
    def __init__(self, name, birth, owner):
        super().__init__("Gato", name, birth)
        self.owner = owner
        self.life_style = "freedom"

    # Imprime dados de cadastro do gato
    def get(self):
        registration_date_formatted = f"Data de Registro: {self.registration_date}"
        name_formatted = f"\nNome: {self.name}"
        race_formatted = f"\nRaça: {self.race}"
        birth_formatted = f"\nNascimento: {self.birth}"
        life_style = f"\nEstilo de vida: {self.life_style}"

        print(f"Dados da {self.name} ------")
        print(registration_date_formatted + name_formatted \
              + race_formatted + birth_formatted + life_style)
