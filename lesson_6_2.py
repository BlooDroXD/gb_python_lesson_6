# 2. Реализовать класс Road (дорога), в котором определить атрибуты:
# length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна. Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т

class Road:

    _length: int
    _width: int

    def __init__(self, length, width):
        self._width = width
        self._length = length

    def calculate_(self, mass_asphalt: int, depth_asphalt: int):
        mass_asphalt = mass_asphalt
        depth_asphalt = depth_asphalt
        return (self._length * self._width * mass_asphalt * depth_asphalt) / 1000


the_road = Road(
    int(input('Введите длину дороги (м): ')),
    int(input('Введите ширину дороги (м): '))
)

mass = int(input('Введите массу асфальта для покрытия одного кв метра дороги (кг): '))
depth = int(input('Введите толщину полотна (см): '))

print(f'{the_road.calculate_(mass, depth)} т')
