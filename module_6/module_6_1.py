class  Animal:
    """Класс животных"""
    alive = True
    fed = False
    def __init__(self, name):
        self.name = name

class  Plant:
    """Класс растений"""
    edible = False
    def __init__(self, name):
        self.name = name

class Mammal(Animal):
    """Класс млекопитающих"""
    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False

class Predator(Animal):
    """Класс хищников"""
    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False

class Flower(Plant):
    """Класс цветов"""
    pass

class Fruit(Plant):
    """Класс фруктов"""
    edible = True

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)
print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)