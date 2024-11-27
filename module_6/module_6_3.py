import random

class Animal:
    """Класс животных"""
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0
    def __init__(self, speed):
        self._cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        x = self._cords[0] + dx * self.speed
        y = self._cords[1] + dy * self.speed
        z = self._cords[2] + dz * self.speed

        if z < 0:
            print("It's too deep, i can't dive :(" )
        else:
            self._cords[0] = x
            self._cords[1] = y
            self._cords[2] = z

    def get_cords(self):
        print(f'X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        if self._DEGREE_OF_DANGER >= 5:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        print(self.sound)

class Bird(Animal):
    """Класс птиц"""
    beak = True

    def lay_eggs(self):
        self.num1_4 = random.randint(1, 4)
        print(f'"Here are(is) {self.num1_4} eggs for you"')

class AquaticAnimal(Animal):
    """Класс плавающих животных"""
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        dz = abs(dz)
        z = self._cords[2] - dz * (self.speed / 2)
        if z < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords[2] = z

class PoisonousAnimal(Animal):
    """Класс ядовитых животных"""
    _DEGREE_OF_DANGER = 8

class Duckbill(PoisonousAnimal, AquaticAnimal, Bird):
    """Класс Утконоса"""
    sound = "Click-click-click"

    def __init__(self, speed):
        super().__init__(speed)

db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()



