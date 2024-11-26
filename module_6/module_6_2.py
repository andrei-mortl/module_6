


class Vehicle:
    """Класс транспорта"""
    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = str(owner)
        self.__model = str(__model)
        self.__engine_power = int(__engine_power)
        self.__color = str(__color)
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def get_model(self):
        print(f'Модель: {self.__model}')

    def get_horsepower(self):
        print(f'Мощность двигателя: {self.__engine_power}')

    def get_color(self):
        print(f'Цвет: {self.__color}')

    def print_info(self):
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        colours = [colour.lower() for colour in self.__COLOR_VARIANTS]  # для проверки без учета регистра
        if new_color.lower() in colours:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')

class Sedan(Vehicle):
    """Класс кузова Седан"""
    __PASSENGERS_LIMIT = 5

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)

vehicle1.set_color('Pink')
vehicle1.set_color('black')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()