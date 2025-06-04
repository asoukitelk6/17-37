'''
1. Создайте базовый класс `Animal`, который будет содержать общие
 атрибуты (например, `name`, `age`) и методы
 (`make_sound()`, `eat()`) для всех животных.

2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и
`Reptile`, которые наследуют от класса `Animal`. Добавьте
специфические атрибуты и переопределите методы, если требуется
(например, различный звук для `make_sound()`).

3. Продемонстрируйте полиморфизм: создайте функцию
`animal_sound(animals)`, которая принимает список животных и
вызывает метод `make_sound()` для каждого животного.

4. Используйте композицию для создания класса `Zoo`, который
будет содержать информацию о животных и сотрудниках. Должны
быть методы для добавления животных и сотрудников в зоопарк.

5. Создайте классы для сотрудников, например, `ZooKeeper`,
`Veterinarian`, которые могут иметь специфические методы
(например, `feed_animal()` для `ZooKeeper` и `heal_animal()`
для `Veterinarian`).

Дополнительно:

Попробуйте добавить дополнительные функции в вашу программу,
такие как сохранение информации о зоопарке в файл и возможность
её загрузки, чтобы у вашего зоопарка было "постоянное состояние"
между запусками программы.'''

class Animal():
    def __init__(self,name='животное',age=1):
        self.name=name
        self.age=age
    def make_sound(self):
        pass
    def eat(self):
        pass
    def __repr__(self):
        return f'{self.__class__.__name__}:{self.name}:{self.age}'

class Bird(Animal):
    def make_sound(self):
        print('карр, чирик и тп')
    def eat(self):
        print('Птица ест')

class Mammal(Animal):
    def make_sound(self):
        print('мяу,гав и тп')
    def eat(self):
        print('Млекопитающее ест')

class Reptile(Animal):
    def make_sound(self):
        print('шшшшш')
    def eat(self):
        print('Рептилия ест')

def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

def eat(animal):
    animal.eat()

class Zoo():
    def __init__(self):
        self.animals=[]
        self.staff=[]
        self.read_file()
    def add_animal(self,animal):
        self.animals.append(animal)
        self.save_file()
        print(f'В зоопарк добавлено новое животное - {animal.name}')
    def add_employee(self,employee):
        self.staff.append(employee)
        print(f'В зоопарк добавлен новый сотрудник - {employee.__class__.__name__}')
    def list_animals(self):
        for animal in self.animals:
            print(f'{animal.__class__.__name__} - {animal.name}, возраст - {animal.age}')

    def save_file(self):
        with open('zoo.txt', 'w',encoding='utf-8') as file:
            for animal in self.animals:
                file.write(repr(animal) + '\n')
    def read_file(self):
        self.animals = []
        with open('zoo.txt', 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(':')
                if len(parts) == 3:
                    class_name, name, age = parts
                    age = int(age)
                    if class_name == 'Bird':
                        animal = Bird(name, age)
                    elif class_name == 'Mammal':
                        animal = Mammal(name, age)
                    elif class_name == 'Reptile':
                        animal = Reptile(name, age)
                    else:
                        continue
                    self.animals.append(animal)


class ZooKeeper():
    def feed_animal(self,animal):
        print(f'Смотритель кормит {animal.name}')

class Veterinarian():
    def heal_animal(self,animal):
        print(f'Ветеринар лечит {animal.name}')

dog=Mammal('собака')
bird=Bird('аист')
reptile=Reptile('рептилия')
dog.eat()

zoo1=Zoo()
keeper=ZooKeeper()
veterinarian=Veterinarian()

zoo1.add_employee(keeper)
zoo1.add_employee(veterinarian)

animal_sound(zoo1.animals)

keeper.feed_animal(zoo1.animals[0])
veterinarian.heal_animal(zoo1.animals[0])

zoo1.list_animals()