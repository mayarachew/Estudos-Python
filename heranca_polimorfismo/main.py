from cat import Cat
from dog import Dog
from datetime import datetime

cat_josefina = Cat("Josefina",datetime.now(),"Jose")
cat_josefina.get()
cat_josefina.calculate_age()

dog_melissa = Dog("Melissa",datetime.now(),"Jose")
dog_melissa.get()
dog_melissa.calculate_age()

